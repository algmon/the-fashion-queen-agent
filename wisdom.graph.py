from typing import Dict, List, Tuple, Any
import networkx as nx
import numpy as np
from dataclasses import dataclass
from enum import Enum

class SpaceType(Enum):
    PERCEPTION = "perception"
    PLANNING = "planning"
    REASONING = "reasoning"
    ACTION = "action"

@dataclass
class WisdomNode:
    id: str
    space_type: SpaceType
    features: Dict[str, Any]  # Flexible storage for space-specific features
    level: int  # Hierarchical level in the graph
    reward: float = 0.0
    probability: float = 1.0

class WisdomGraph:
    def __init__(self):
        # Separate graphs for each space for optimized processing
        self.perception_graph = nx.DiGraph()
        self.planning_graph = nx.DiGraph()
        self.reasoning_graph = nx.DiGraph()
        self.action_graph = nx.DiGraph()

        # Mapping between spaces
        self.cross_space_edges = nx.DiGraph()

    def add_perception_node(self, node_id: str, features: Dict[str, Any], level: int) -> None:
        """Add a node in perception space (e.g., visual or audio features)"""
        node = WisdomNode(
            id=node_id,
            space_type=SpaceType.PERCEPTION,
            features=features,
            level=level
        )
        self.perception_graph.add_node(node_id, data=node)

    def add_planning_node(self, node_id: str, task_info: Dict[str, Any], level: int) -> None:
        """Add a node in planning space (task hierarchies)"""
        node = WisdomNode(
            id=node_id,
            space_type=SpaceType.PLANNING,
            features=task_info,
            level=level
        )
        self.planning_graph.add_node(node_id, data=node)

    def add_reasoning_node(self, node_id: str, variables: Dict[str, Any],
                          probability: float, level: int) -> None:
        """Add a node in reasoning space (Bayesian network nodes)"""
        node = WisdomNode(
            id=node_id,
            space_type=SpaceType.REASONING,
            features=variables,
            level=level,
            probability=probability
        )
        self.reasoning_graph.add_node(node_id, data=node)

    def add_action_node(self, node_id: str, state_info: Dict[str, Any],
                       reward: float, level: int) -> None:
        """Add a node in action space (Q-learning states)"""
        node = WisdomNode(
            id=node_id,
            space_type=SpaceType.ACTION,
            features=state_info,
            level=level,
            reward=reward
        )
        self.action_graph.add_node(node_id, data=node)

    def add_edge_within_space(self, space_type: SpaceType, source_id: str,
                            target_id: str, weight: float = 1.0) -> None:
        """Add an edge within a specific space"""
        graph = getattr(self, f"{space_type.value}_graph")
        if source_id in graph and target_id in graph:
            graph.add_edge(source_id, target_id, weight=weight)

    def add_cross_space_edge(self, source_id: str, target_id: str,
                            source_space: SpaceType, target_space: SpaceType) -> None:
        """Connect nodes across different spaces"""
        self.cross_space_edges.add_edge(
            source_id,
            target_id,
            source_space=source_space,
            target_space=target_space
        )

    def prune_perception_space(self, feature_threshold: float) -> None:
        """Prune nodes in perception space based on feature importance"""
        nodes_to_remove = []
        for node_id, data in self.perception_graph.nodes(data=True):
            feature_importance = np.mean(list(data['data'].features.values()))
            if feature_importance < feature_threshold:
                nodes_to_remove.append(node_id)
        self.perception_graph.remove_nodes_from(nodes_to_remove)

    def prune_planning_space(self, efficiency_threshold: float) -> None:
        """Prune inefficient subtasks in planning space"""
        nodes_to_remove = []
        for node_id, data in self.planning_graph.nodes(data=True):
            if data['data'].features.get('efficiency', 0) < efficiency_threshold:
                nodes_to_remove.append(node_id)
        self.planning_graph.remove_nodes_from(nodes_to_remove)

    def prune_reasoning_space(self, probability_threshold: float) -> None:
        """Prune less influential nodes in reasoning space"""
        nodes_to_remove = []
        for node_id, data in self.reasoning_graph.nodes(data=True):
            if data['data'].probability < probability_threshold:
                nodes_to_remove.append(node_id)
        self.reasoning_graph.remove_nodes_from(nodes_to_remove)

    def prune_action_space(self, reward_threshold: float) -> None:
        """Prune low-reward actions"""
        nodes_to_remove = []
        for node_id, data in self.action_graph.nodes(data=True):
            if data['data'].reward < reward_threshold:
                nodes_to_remove.append(node_id)
        self.action_graph.remove_nodes_from(nodes_to_remove)

    def update_q_value(self, state_id: str, action_id: str, reward: float,
                      learning_rate: float = 0.1) -> None:
        """Update Q-values in action space"""
        if state_id in self.action_graph and action_id in self.action_graph:
            current_q = self.action_graph.nodes[state_id]['data'].reward
            new_q = current_q + learning_rate * (reward - current_q)
            self.action_graph.nodes[state_id]['data'].reward = new_q

    def get_highest_reward_action(self, state_id: str) -> str:
        """Get the action with highest reward for a given state"""
        if state_id not in self.action_graph:
            return None

        successors = list(self.action_graph.successors(state_id))
        if not successors:
            return None

        return max(
            successors,
            key=lambda x: self.action_graph.nodes[x]['data'].reward
        )
