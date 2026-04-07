# Smart Irrigation RL Environment

## Problem Statement
Farmers often overwater or underwater crops due to lack of real-time decision systems.

## Solution
We built a reinforcement learning environment that optimizes irrigation decisions based on soil moisture and weather conditions.

## RL Formulation
- State: soil moisture, weather
- Actions: no water, low, medium, high
- Reward: based on maintaining optimal soil moisture (40–70%)

## Metrics
- Efficiency Score
- Stability Score

## How to Run
python env.py