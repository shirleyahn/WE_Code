main_directory='/scratch/users/sahn1/WE_2D_Toy_Model'

balls_flag=0  # 0: create new balls at each step. 1: keep created balls.
sorting_flag=1  # 0: sort walkers' weights in descending order (most probable walkers first). 1: sort walkers' weights in
              # ascending order (rare walkers first).
rate_flag=1  # 0: off. 1: on. rates/fluxes between pre-defined states  will be calculated. the walker's state is
           #  determined by we_check_state_function.py.
num_states=2  # number of pre-defined states for rate/flux calculation. only needed if rate_flag = 1, otherwise 1.
enhanced_sampling_flag=2  # 0: off. 1: sub-binning balls by standard deviation distance from center of ball. 2: binning
                        # walkers if the walkers have some property less or greater than threshold. 3: spectral
                        # clustering.

num_balls_limit=100000  # limit is set depending on the available memory. parameter needed in case the calculated max_num_balls
                 # is greater or too much smaller than the limit.
radius=0.1  # radius can be changed in the middle of the simulation.
num_walkers=100  # num_walkers should be fixed.
num_cvs=2  # number of collective variables (num_cvs) should be fixed.
grid_dimensions=[-1.0, 1.0, -1.0, 1.0]  # since num_cvs = 2, then type x_lower_bound x_upper_bound y_lower_bound y_upper_bound

max_num_steps=200  # maximum number of steps for the simulation.
num_occupied_balls=1  # num_occupied_balls should be changed when restarting a simulation.

m_steps_per_step=5  # how many times the metropolis algorithm should be executed per step
step_size=0.05  # how large the step size should be for each walker
beta=10.0  # inverse temperature
pbc=1  # 0: off. 1: periodic boundary conditions on.

### for the next four lines, if enhanced_sampling_flag = 2 ###
less_or_greater_flag=0  # 0: criteria for binning walkers is if the walkers have some property LESS than the threshold.
                      # 1: criteria for binning walkers is if the walkers have some property GREATER than the threshold.
static_threshold_flag=1  # 0: off, then the lowest (less_or_greater_flag = 0) or highest (less_or_greater_flag = 1)
                       # current value is set as the threshold for the next step. 1: on, initial threshold is kept
                       # throughout the simulation.
threshold_values=[1.0e-100]  # if some properties of the walker have
                  # values less or greater than the threshold values, then it is
                  # binned to the nearest existing ball.
properties_to_keep_track=[-1]  # properties of the
                          # walker that are compared against the threshold values. this can be weight
                          # and/or some collective variable(s). if one of them is weight, then type -1. otherwise type
                          # the indices of the collective variable, e.g. if there are 3 collective variables and you
                          # would like to keep track of the last one, type 2
                          # (index starts from 0). if more than one property is kept track of, then type them sequentially

### for the next three lines, if enhanced_sampling flag == 3 ###
num_balls_for_sc=100  # minimum number of balls present to perform spectral clustering for that step
num_clusters=10  # number of clusters for k-means part of spectral clustering
num_walkers_for_sc=100  # number of walkers for each macrostate, usually set equal to the avg number of walkers per
                    # macrostate, which is (num_balls_for_sc/num_clusters)*num_walkers