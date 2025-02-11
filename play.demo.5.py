from agent import FashionAgent
from env import FashionRoomEnv


def main():
    # Initialize environment and agents
    fashion_room = FashionRoomEnv()
    fashion_agent_1 = FashionAgent()
    fashion_agent_2 = FashionAgent()
    fashion_agent_3 = FashionAgent()
    fashion_agent_4 = FashionAgent()

    # Set different specializations for each agent
    fashion_agent_1.core_task = "good team member and good for online and offline sales"
    fashion_agent_2.core_task = "good team member and good for taking beautiful photos and videos"
    fashion_agent_3.core_task = "good team member and good for new media creation such as news, blog posts"
    fashion_agent_4.core_task = "good team member and good for fashion goods selection, import and export"

    # Initialize team workflow
    team_workflow = {
        "product_cycle": [
            {
                "phase": "product_selection",
                "lead": fashion_agent_4,
                "supporters": [fashion_agent_1],
                "tasks": ["market_research", "trend_analysis", "supplier_negotiation"]
            },
            {
                "phase": "content_creation",
                "lead": fashion_agent_2,
                "supporters": [fashion_agent_3],
                "tasks": ["photo_shooting", "video_production", "content_editing"]
            },
            {
                "phase": "media_distribution",
                "lead": fashion_agent_3,
                "supporters": [fashion_agent_2],
                "tasks": ["story_writing", "social_media_posting", "blog_creation"]
            },
            {
                "phase": "sales_execution",
                "lead": fashion_agent_1,
                "supporters": [fashion_agent_4],
                "tasks": ["online_promotion", "offline_display", "customer_service"]
            }
        ]
    }

    print("Demo 5: Fashion Team Collaboration")
    print("----------------------------------")

    # Process each phase in the product cycle
    for phase in team_workflow["product_cycle"]:
        print(f"\nExecuting Phase: {phase['phase']}")

        # 1. Perception Phase - Gather information
        perception_data = gather_team_perception(
            phase["lead"],
            phase["supporters"],
            fashion_room
        )
        print("Perception Phase Complete")

        '''
        # 2. Planning Phase - Create strategies
        phase_plans = create_team_plans(
            phase["lead"],
            phase["supporters"],
            perception_data,
            phase["tasks"]
        )
        print("Planning Phase Complete")

        # 3. Reasoning Phase - Make decisions
        team_decisions = reason_about_execution(
            phase["lead"],
            phase["supporters"],
            phase_plans,
            perception_data
        )
        print("Reasoning Phase Complete")

        # 4. Action Phase - Execute decisions
        execute_team_actions(
            phase["lead"],
            phase["supporters"],
            team_decisions,
            fashion_room
        )
        print("Action Phase Complete")
        '''


def gather_team_perception(lead_agent, support_agents, environment):
    """Perception phase - gather and combine team observations"""
    perception_data = {
        "market": lead_agent.wisdom.perception_graph.analyze_market(),
        "trends": lead_agent.wisdom.perception_graph.analyze_trends(),
        "customer_needs": lead_agent.wisdom.perception_graph.analyze_customers()
    }

    # Add supporter perceptions
    for supporter in support_agents:
        supporter_data = supporter.wisdom.perception_graph.gather_insights()
        perception_data.update(supporter_data)

    # Add environmental observations
    perception_data["environment"] = environment.get_current_state()

    return perception_data


def create_team_plans(lead_agent, support_agents, perception_data, tasks):
    """Planning phase - develop coordinated strategies"""
    # Lead agent creates main strategy
    main_plan = lead_agent.wisdom.planning_graph.create_strategy(
        perception_data,
        tasks
    )

    # Support agents create complementary plans
    support_plans = []
    for supporter in support_agents:
        support_plan = supporter.wisdom.planning_graph.create_support_plan(
            perception_data,
            main_plan,
            tasks
        )
        support_plans.append(support_plan)

    return {
        "main_plan": main_plan,
        "support_plans": support_plans
    }


def reason_about_execution(lead_agent, support_agents, plans, perception_data):
    """Reasoning phase - evaluate and optimize execution plans"""
    # Lead agent evaluates overall strategy
    strategy_evaluation = lead_agent.wisdom.reasoning_graph.evaluate_strategy(
        plans["main_plan"],
        perception_data
    )

    # Support agents contribute insights
    support_evaluations = []
    for supporter in support_agents:
        support_eval = supporter.wisdom.reasoning_graph.evaluate_support(
            plans["support_plans"],
            perception_data
        )
        support_evaluations.append(support_eval)

    # Combine evaluations into final decisions
    return {
        "strategy": optimize_strategy(strategy_evaluation, support_evaluations),
        "coordination": create_coordination_plan(strategy_evaluation, support_evaluations),
        "risk_management": assess_risks(strategy_evaluation, support_evaluations)
    }


def execute_team_actions(lead_agent, support_agents, decisions, environment):
    """Action phase - coordinated execution of decisions"""
    # Lead agent initiates main actions
    lead_agent.wisdom.action_graph.execute_strategy(
        decisions["strategy"],
        environment
    )

    # Support agents execute supporting actions
    for supporter in support_agents:
        supporter.wisdom.action_graph.execute_support_actions(
            decisions["coordination"],
            environment
        )

    # Update environment state
    environment.update_state(decisions["strategy"])


if __name__ == "__main__":
    main()
