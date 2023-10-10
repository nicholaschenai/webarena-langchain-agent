from browser_env import (
    ScriptBrowserEnv,
    Trajectory,
)


def init(args):
    global env, trajectory, state_info, render_helper, meta_data, llm_response, tool_error_start, parse_error_start
    env = ScriptBrowserEnv(
        headless=not args.render,
        slow_mo=args.slow_mo,
        observation_type=args.observation_type,
        current_viewport_only=args.current_viewport_only,
        viewport_size={
            "width": args.viewport_width,
            "height": args.viewport_height,
        },
        save_trace_enabled=args.save_trace_enabled,
        sleep_after_execution=args.sleep_after_execution,
    )
    trajectory = []
    state_info = {}
    render_helper = None
    meta_data = {"action_history": ["None"]}
    llm_response = ""
    tool_error_start = "The following errors occurred during tool execution:"
    parse_error_start = "Parsing error. Please check your inputs and function and try again. The error message is "


