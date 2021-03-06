import numpy as np


class PIDController:

    def __init__(self, k_p, k_i, k_d, num_timesteps):
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d
        self.prev_error_list = [0] * num_timesteps
        self.error_list_counter = 0

    def errorFunction(self, error):  # needs renaming "update input value" or something
        # calls each of the three functions below and adds their result
        return

    def __proportional_controller__(self, error):
        pass

    def __integral_controller__(self, preverror):
        # compute sum of previous error values
        pass

    def __derivative_controller__(self, error):
        pass


class LinearSpeedPIDController(PIDController):

    def __proportional_controller__(self, error):
        # needs to calculate a new p term based on a unique error function for controlling linear speed
        # like sqrt(error) or something like that
        pass


class AngularSpeedPIDController(PIDController):

    def __proportional_controller__(self, error):
        # needs to calculate a new p term based on a unique error function for controlling angular speed
        # like sqrt(error) or something like that
        pass


if __name__ == "__main__":
    exit()
