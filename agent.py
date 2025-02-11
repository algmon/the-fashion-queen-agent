from graph import WisdomGraph, SpaceType, WisdomNode
from env import Env


class Agent:
    # core variables
    def __init__(self):
        self.autopilot_provider = "Suanfamama"
        self.autopilot = 0
        self.brain_provider = "Suanfamama"
        self.body_provider = "Suanfamama"
        self.designed_for = ["general_purpose_complex_tasks"]
        self.intelligence = 0
        self.sub_class = "intelligent robot"
        self.core_task = ""
        self.tasks_waiting_list = ["", "", ""]
        self.states = []  # unified graph based action and state dynamic map with probability computation in real time
        self.actions = []
        self.solver_provider = "Suanfamama"
        self.solver = 0
        # for natural language processing - mostly language translation
        self.nlp_provider = "Suanfamama"
        self.nlp = 0
        self.cv_provider = "Suanfamama"
        self.cv = 0
        self.perception_provider = "Suanfamama"
        self.perception = 0
        self.planner_provider = "Suanfamama"
        self.planning = 0
        self.reasoning_provider = "Suanfamama"
        self.reasoning = 0
        self.action_provider = "Suanfamama"
        self.action = 0
        self.search_provider = "Suanfamama"
        self.search = 0
        self.capability = 0
        self.responsibility = 0
        self.knowledge_provider = "Suanfamama"
        self.knowledge = 0
        self.energy_provider = "Suanfamama"
        self.energy = 0
        self.money_provider = "Suanfamama"
        self.money = 0
        self.time_provider = "Suanfamama"
        self.time = 0
        self.memory_provider = "Suanfamama"
        self.memory = 0
        self.protect_provider = "Suanfamama"
        self.protect = 0
        self.friends = 0
        self.enemies = 0
        self.family = 0
        self.history_provider = "Suanfamama"
        self.history = 0


class FashionAgent(Agent):
    def __init__(self):
        super().__init__()
        self.wisdom = WisdomGraph()
        self.core_task = "being_fashion_and_earn_fortune"

        # Add team collaboration attributes
        self.team_role = None
        self.current_phase = None

        # Initialize the wisdom graph spaces
        self._init_perception_space()
        self._init_planning_space()
        self._init_reasoning_space()
        self._init_action_space()

    def _init_perception_space(self):
        """Initialize perception nodes for fashion vision"""
        # Initialize market perception nodes
        market_node = WisdomNode(
            id="market_analysis",
            space_type=SpaceType.PERCEPTION,
            features={
                "market_size": 1000000,
                "competition": 0.7,
                "growth": 0.3,
                "trends": ["sustainable", "digital_first"]
            },
            level=1
        )
        self.wisdom.perception_graph.add_node(
            "market_analysis", data=market_node)
        self.wisdom.perception_graph.market_nodes.append("market_analysis")

        # Initialize trend perception nodes
        trend_node = WisdomNode(
            id="trend_analysis",
            space_type=SpaceType.PERCEPTION,
            features={
                "current": ["minimalism", "eco-friendly"],
                "emerging": ["smart-fashion", "customization"],
                "strength": {"minimalism": 0.8, "eco-friendly": 0.7},
                "duration": {"minimalism": 12, "eco-friendly": 24}
            },
            level=1
        )
        self.wisdom.perception_graph.add_node(
            "trend_analysis", data=trend_node)
        self.wisdom.perception_graph.trend_nodes.append("trend_analysis")

        # Initialize customer perception nodes
        customer_node = WisdomNode(
            id="customer_analysis",
            space_type=SpaceType.PERCEPTION,
            features={
                "preferences": {"style": "modern", "price_range": "mid-high"},
                "patterns": ["online_shopping", "social_media_influenced"],
                "satisfaction": {"product_quality": 0.85, "service": 0.9},
                "demographics": {"age_group": "25-35", "income": "upper-middle"}
            },
            level=1
        )
        self.wisdom.perception_graph.add_node(
            "customer_analysis", data=customer_node)
        self.wisdom.perception_graph.customer_nodes.append("customer_analysis")

    def _init_planning_space(self):
        """Initialize planning hierarchy for fashion tasks"""
        self.wisdom.add_planning_node(
            "plan_composition",
            task_info={
                "priority": 1,
                "type": "aesthetic_composition",
                "subtasks": ["color_balance", "pattern_harmony"]
            },
            level=1
        )

        self.wisdom.add_planning_node(
            "plan_style_analysis",
            task_info={
                "priority": 2,
                "type": "style_categorization",
                "subtasks": ["trend_analysis", "style_matching"]
            },
            level=2
        )

        self.wisdom.add_planning_node(
            "plan_sharing",
            task_info={
                "priority": 3,
                "type": "content_sharing",
                "subtasks": ["audience_targeting", "platform_selection"]
            },
            level=3
        )

    def _init_reasoning_space(self):
        """Initialize reasoning nodes for fashion decisions"""
        self.wisdom.add_reasoning_node(
            "reason_aesthetic_value",
            variables={
                "color_harmony": 0.0,
                "pattern_balance": 0.0,
                "composition_score": 0.0
            },
            probability=0.8,
            level=1
        )

        self.wisdom.add_reasoning_node(
            "reason_trend_relevance",
            variables={
                "trend_alignment": 0.0,
                "seasonal_fit": 0.0,
                "audience_appeal": 0.0
            },
            probability=0.7,
            level=2
        )

        self.wisdom.add_reasoning_node(
            "reason_sharing_strategy",
            variables={
                "platform_suitability": 0.0,
                "timing_optimization": 0.0,
                "audience_engagement": 0.0
            },
            probability=0.9,
            level=3
        )

    def _init_action_space(self):
        """Initialize action space for fashion tasks"""
        actions = [
            ("capture_image", {"type": "photography", "settings": {}}),
            ("edit_image", {"type": "post_processing", "filters": []}),
            ("analyze_style", {"type": "style_analysis", "parameters": {}}),
            ("share_content", {"type": "social_sharing", "platform": None})
        ]

        for action_id, state_info in actions:
            self.wisdom.add_action_node(
                action_id,
                state_info=state_info,
                reward=0.0,
                level=1
            )

    def process_fashion_item(self, image_data):
        """Main function to process a fashion item"""
        # Update perception
        self._update_visual_perception(image_data)

        # Planning phase
        composition_plan = self._plan_composition()
        style_plan = self._plan_style_analysis()
        sharing_plan = self._plan_content_sharing()

        # Reasoning phase
        action_decision = self._reason_about_actions(
            composition_plan,
            style_plan,
            sharing_plan
        )

        # Execute action and update rewards
        result = self._execute_action(action_decision)
        self._update_action_rewards(action_decision, result)

        return result

    def _update_visual_perception(self, image_data):
        """Update perception nodes with new image data"""
        # Update color perception
        self.wisdom.perception_graph.nodes["vision_colors"]["data"].features.update(
            self._analyze_colors(image_data)
        )

        # Update pattern perception
        self.wisdom.perception_graph.nodes["vision_patterns"]["data"].features.update(
            self._analyze_patterns(image_data)
        )

        # Update style perception
        self.wisdom.perception_graph.nodes["vision_style"]["data"].features.update(
            self._analyze_style(image_data)
        )

    def _reason_about_actions(self, composition_plan, style_plan, sharing_plan):
        """Combine different aspects to make final decision"""
        # Update reasoning nodes with new information
        self.wisdom.reasoning_graph.nodes["reason_aesthetic_value"]["data"].variables.update(
            self._evaluate_aesthetics(composition_plan)
        )

        self.wisdom.reasoning_graph.nodes["reason_trend_relevance"]["data"].variables.update(
            self._evaluate_trends(style_plan)
        )

        self.wisdom.reasoning_graph.nodes["reason_sharing_strategy"]["data"].variables.update(
            self._evaluate_sharing(sharing_plan)
        )

        return self._select_best_action()

    def plan_phase(self, tasks):
        """Plan execution strategy for a phase"""
        strategy = {
            "strategy": {
                "name": self.current_phase,
                "tasks": tasks,
                "execution_order": [],
                "resource_allocation": {},
                "timeline": {},
                "actions": [],
                "coordination_points": {}
            }
        }

        # Use wisdom graph for planning
        for task in tasks:
            # Get relevant planning nodes
            plan_nodes = self._get_relevant_planning_nodes(task)

            # Use reasoning nodes to evaluate best approach
            task_strategy = self._reason_about_task(task, plan_nodes)

            strategy["strategy"]["execution_order"].append(task)
            strategy["strategy"]["resource_allocation"][task] = task_strategy["resources"]
            strategy["strategy"]["timeline"][task] = task_strategy["timeline"]
            strategy["strategy"]["actions"].extend(task_strategy["actions"])
            strategy["strategy"]["coordination_points"].update(
                task_strategy["coordination"])

        return strategy

    def support_phase(self, tasks):
        """Provide support planning for a phase"""
        support_plan = {
            "actions": [],
            "coordination_points": {}
        }

        # Use wisdom graph for support planning
        for task in tasks:
            # Get relevant support capabilities
            support_capabilities = self._get_support_capabilities(task)

            # Plan support actions
            task_support = self._plan_support_actions(
                task, support_capabilities)

            support_plan["actions"].extend(task_support["actions"])
            support_plan["coordination_points"].update(
                task_support["coordination"])

        return support_plan

    def _get_relevant_planning_nodes(self, task):
        """Get planning nodes relevant to the task"""
        relevant_nodes = []
        for node_id in self.wisdom.planning_graph.nodes():
            node_data = self.wisdom.planning_graph.nodes[node_id]["data"]
            if task in node_data.features.get("subtasks", []):
                relevant_nodes.append(node_data)
        return relevant_nodes

    def _reason_about_task(self, task, plan_nodes):
        """Use reasoning to develop task strategy"""
        strategy = {
            "resources": {},
            "timeline": {},
            "actions": [],
            "coordination": {}
        }

        # Use reasoning nodes to evaluate approach
        for node in plan_nodes:
            task_evaluation = self._evaluate_task_approach(task, node)
            strategy["resources"].update(task_evaluation["required_resources"])
            strategy["timeline"].update(task_evaluation["estimated_timeline"])
            strategy["actions"].extend(task_evaluation["recommended_actions"])
            strategy["coordination"].update(
                task_evaluation["coordination_needs"])

        return strategy

    def _get_support_capabilities(self, task):
        """Identify relevant support capabilities for a task"""
        capabilities = []
        # Query wisdom graph for relevant capabilities
        for node_id in self.wisdom.action_graph.nodes():
            node_data = self.wisdom.action_graph.nodes[node_id]["data"]
            if self._is_relevant_for_support(task, node_data):
                capabilities.append(node_data)
        return capabilities

    def _plan_support_actions(self, task, capabilities):
        """Plan specific support actions"""
        support = {
            "actions": [],
            "coordination": {}
        }

        for capability in capabilities:
            support_action = self._create_support_action(task, capability)
            support["actions"].append(support_action["action"])
            support["coordination"].update(support_action["coordination"])

        return support

    def _is_relevant_for_support(self, task, node_data):
        """Check if a capability is relevant for supporting a task"""
        task_keywords = set(task.split("_"))
        capability_keywords = set(str(node_data.features).split("_"))
        return bool(task_keywords & capability_keywords)

    def _create_support_action(self, task, capability):
        """Create a specific support action based on capability"""
        return {
            "action": {
                "type": "support",
                "task": task,
                "capability": capability.id,
                "parameters": self._get_support_parameters(task, capability)
            },
            "coordination": {
                f"coord_{task}_{capability.id}": {
                    "timing": "as_needed",
                    "resources": "shared",
                    "communication": "continuous"
                }
            }
        }

    def _get_support_parameters(self, task, capability):
        """Get specific parameters for a support action"""
        return {
            "priority": self._calculate_priority(task, capability),
            "resource_allocation": self._calculate_resources(task, capability),
            "timing": self._determine_timing(task, capability)
        }


class EducationAgent(Agent):
    def __init__(self):
        super().__init__()
        self.wisdom = WisdomGraph()
        self.core_task = "being_inspired_and_create_wisdom"

        # Initialize the wisdom graph spaces
        self._init_perception_space()
        self._init_planning_space()
        self._init_reasoning_space()
        self._init_action_space()

    def _init_perception_space(self):
        """Initialize perception nodes for education"""
        # Student engagement perception
        self.wisdom.add_perception_node(
            "student_engagement",
            features={
                "attention_level": 0.0,
                "participation_rate": 0.0,
                "interaction_patterns": []
            },
            level=1
        )

        # Learning environment perception
        self.wisdom.add_perception_node(
            "environment_state",
            features={
                "noise_level": 0.0,
                "lighting_quality": 0.0,
                "room_temperature": 22.0,
                "space_utilization": 0.0
            },
            level=1
        )

        # Learning progress perception
        self.wisdom.add_perception_node(
            "learning_progress",
            features={
                "comprehension_indicators": [],
                "skill_development_metrics": {},
                "knowledge_retention_rates": {}
            },
            level=2
        )

    def _init_planning_space(self):
        """Initialize planning hierarchy for education"""
        self.wisdom.add_planning_node(
            "lesson_planning",
            task_info={
                "priority": 1,
                "type": "curriculum_execution",
                "subtasks": ["content_delivery", "activity_management"]
            },
            level=1
        )

        self.wisdom.add_planning_node(
            "engagement_strategy",
            task_info={
                "priority": 2,
                "type": "student_engagement",
                "subtasks": ["interaction_design", "motivation_management"]
            },
            level=2
        )

        self.wisdom.add_planning_node(
            "assessment_planning",
            task_info={
                "priority": 3,
                "type": "learning_evaluation",
                "subtasks": ["progress_tracking", "feedback_generation"]
            },
            level=2
        )

    def _init_reasoning_space(self):
        """Initialize reasoning nodes for educational decisions"""
        self.wisdom.add_reasoning_node(
            "learning_effectiveness",
            variables={
                "content_comprehension": 0.0,
                "skill_application": 0.0,
                "knowledge_integration": 0.0
            },
            probability=0.8,
            level=1
        )

        self.wisdom.add_reasoning_node(
            "student_needs",
            variables={
                "learning_style_match": 0.0,
                "difficulty_adjustment": 0.0,
                "support_requirements": 0.0
            },
            probability=0.7,
            level=2
        )

        self.wisdom.add_reasoning_node(
            "environmental_optimization",
            variables={
                "space_configuration": 0.0,
                "resource_utilization": 0.0,
                "ambient_conditions": 0.0
            },
            probability=0.9,
            level=1
        )

    def _init_action_space(self):
        """Initialize action space for educational tasks"""
        actions = [
            ("adjust_content", {
             "type": "content_modification", "parameters": {}}),
            ("modify_environment", {
             "type": "environment_control", "settings": {}}),
            ("provide_feedback", {"type": "student_feedback", "format": None}),
            ("implement_activity", {
             "type": "learning_activity", "structure": {}})
        ]

        for action_id, state_info in actions:
            self.wisdom.add_action_node(
                action_id,
                state_info=state_info,
                reward=0.0,
                level=1
            )

    def facilitate_learning(self, classroom_data):
        """Main function to manage learning process"""
        # Update perception
        self._update_learning_perception(classroom_data)

        # Planning phase
        lesson_plan = self._plan_lesson_execution()
        engagement_plan = self._plan_engagement_strategy()
        assessment_plan = self._plan_assessment()

        # Reasoning phase
        action_decision = self._reason_about_actions(
            lesson_plan,
            engagement_plan,
            assessment_plan
        )

        # Execute action and update rewards
        result = self._execute_action(action_decision)
        self._update_action_rewards(action_decision, result)

        return result

    def _update_learning_perception(self, classroom_data):
        """Update perception nodes with classroom data"""
        if "student_metrics" in classroom_data:
            self.wisdom.perception_graph.nodes["student_engagement"]["data"].features.update(
                self._analyze_engagement(classroom_data["student_metrics"])
            )

        if "environment_metrics" in classroom_data:
            self.wisdom.perception_graph.nodes["environment_state"]["data"].features.update(
                self._analyze_environment(
                    classroom_data["environment_metrics"])
            )

        if "progress_metrics" in classroom_data:
            self.wisdom.perception_graph.nodes["learning_progress"]["data"].features.update(
                self._analyze_progress(classroom_data["progress_metrics"])
            )

    def _reason_about_actions(self, lesson_plan, engagement_plan, assessment_plan):
        """Combine different aspects to make final decision"""
        # Update reasoning nodes with new information
        self.wisdom.reasoning_graph.nodes["learning_effectiveness"]["data"].variables.update(
            self._evaluate_effectiveness(lesson_plan)
        )

        self.wisdom.reasoning_graph.nodes["student_needs"]["data"].variables.update(
            self._evaluate_needs(engagement_plan)
        )

        self.wisdom.reasoning_graph.nodes["environmental_optimization"]["data"].variables.update(
            self._evaluate_environment(assessment_plan)
        )

        return self._select_best_action()
