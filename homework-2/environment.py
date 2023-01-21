import random
import time

import gym
from gym import spaces
import pygame

import settings


class Arm:
    def __init__(self, p=0, earn=0):
        self.probability = p
        self.earn = earn

    def execute(self):
        return self.earn if random.random() < self.probability else 0


class TwoArmedBanditEnv(gym.Env):
    def __init__(self):
        self.delay = 0.5
        self.arms = (Arm(0.5, 1), Arm(0.1, 100))
        self.observation_space = spaces.Discrete(1)
        self.action_space = spaces.Discrete(len(self.arms))
        pygame.init()
        pygame.display.init()
        self.window = pygame.display.set_mode(
            (settings.WINDOW_WIDTH, settings.WINDOWS_HEIGHT))
        pygame.display.set_caption("Two-Armed Bandit Environment")
        self.action = None
        self.last_action = None
        self.reward = None
        self.total_reward = 0
        self.reward_1 = 0
        self.reward_2 = 0

        self.reward_earm1 = "Earn 1"
        self.reward_earm2 = "Earn 2"
        self.total_reward_ = "Total"

    def _get_obs(self):
        return 0

    def _get_info(self):
        return {'state': 0}

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        if options is not None:
            if type(options) is not dict:
                raise RuntimeError("Variable options is not a dictionary")
            self.delay = options.get('delay', 0.5)

        observation = self._get_obs()
        info = self._get_info()
        return observation, info

    def step(self, action):
        self.last_action = self.action
        self.action = action
        self.reward = self.arms[action].execute()
        if action == 0:
            self.reward_1 += self.reward
        elif action == 1:
            self.reward_2 += self.reward
        self.total_reward += self.reward
        observation = self._get_obs()
        info = self._get_info()

        self.render()
        time.sleep(self.delay)

        return observation, self.reward, False, False, info

    def _render_props(self):
        if self.reward is None or self.action is None:
            return

        x = 250 + settings.MACHINE_WIDTH / 2

        if self.action == 1:
            x += 250 + settings.MACHINE_WIDTH

        # Render the reward
        font = settings.FONTS['large']
        text_obj = font.render(f"{self.reward}", True, (0, 0, 0))
        text_rect = text_obj.get_rect()
        text_rect.center = (x, 80)
        self.window.blit(text_obj, text_rect)

        # Render the action total reward
        index = settings.TEXTURES['index']
        w, h = index.get_size()
        self.window.blit(index, (634, 5))

        # Render earn machine 1
        index = settings.TEXTURES['index']
        w, h = index.get_size()
        self.window.blit(index, (0, 264))

        font = settings.FONTS['large2']
        text_obj = font.render(f"{self.reward_1}", True, (0, 0, 0))
        text_rect = text_obj.get_rect()
        text_rect.center = (132, 360)
        self.window.blit(text_obj, text_rect)

        self.window.blit(font.render(
            f"{self.reward_earm1}", True, (0, 0, 0)), (10, 200))

        # Render earn machine 2
        index = settings.TEXTURES['index']
        w, h = index.get_size()
        self.window.blit(index, (1256, 264))

        font = settings.FONTS['large2']
        text_obj = font.render(f"{self.reward_2}", True, (0, 0, 0))
        text_rect = text_obj.get_rect()
        text_rect.center = (1388, 360)
        self.window.blit(text_obj, text_rect)

        self.window.blit(font.render(
            f"{self.reward_earm2}", True, (0, 0, 0)), (1280, 200))

        # Render the total reward
        font = settings.FONTS['large2']
        text_obj = font.render(f"{self.total_reward}", True, (0, 0, 0))
        text_rect = text_obj.get_rect()
        text_rect.center = (766, 100)
        self.window.blit(text_obj, text_rect)

        self.window.blit(font.render(
            f"{self.total_reward_}", True, (0, 0, 0)), (660, 250))

        # Render the action
        arrow = settings.TEXTURES['arrow']
        if self.action == self.last_action:
            self.window.blit(
                arrow, (-100, 0))
            pygame.display.update()
            time.sleep(self.delay)
            w, h = arrow.get_size()
            self.window.blit(arrow, (x - w / 2 - 80, 250 +
                                     settings.MACHINE_HEIGHT - h / 2))
        else:
            w, h = arrow.get_size()
            self.window.blit(arrow, (x - w / 2 - 80, 250 +
                                     settings.MACHINE_HEIGHT - h / 2))

    def render(self):
        self.window.fill((255, 255, 255))

        # Render the first machine
        self.window.blit(settings.TEXTURES['machine'], (250, 150))

        # Render the second machine
        self.window.blit(
            settings.TEXTURES['machine'], (400 + settings.MACHINE_WIDTH, 150))

        self._render_props()

        pygame.event.pump()
        pygame.display.update()

    def close(self):
        pygame.display.quit()
        pygame.font.quit()
        pygame.quit()
