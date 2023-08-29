import pprint

from dyna_gym.pipelines import uct_for_hf_transformer_pipeline


def length_reward_func(input_str: str) -> float:
    # the shorter, the better
    return -len(input_str)

horizon = 100

uct_args = dict(
    rollouts = 5,
    gamma = 1.,
    width = 3,
    alg = 'uct',
)

model_generation_args = dict(
    do_sample = True,
    temperature = 0.7,
)

input_str = "Hello, I'm a language model,"
pipeline = uct_for_hf_transformer_pipeline(
    model_name = "gpt2",
    horizon = horizon,
    reward_func = length_reward_func,
    uct_args = uct_args,
    model_generation_args = model_generation_args,
    should_plot_tree = True,
)
outputs = pipeline(input_str)

# outputs are samples generated by the UCT agent
pprint.pprint(outputs)