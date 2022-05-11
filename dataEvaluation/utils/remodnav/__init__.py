import logging
import numpy as np
from .clf import EyeGazeClassifier, deg_per_pixel

lgr = logging.getLogger('remodnav')

help = {
    'dilate_nan': """duration for which to replace data by missing data
    markers on either side of a signal-loss window (in seconds)""",
    'lowpass_cutoff_freq': """cut-off frequency of a Butterworth low-pass
    filter applied to determine drift velocities in a pursuit event
    candidate (in Hz)""",
    'max_initial_saccade_freq': """maximum saccade frequency for initial
    detection of major saccades, initial data chunking is stopped if this
    frequency is reached (should be smaller than an expected (natural)
    saccade frequency in a particular context) (in Hz)""",
    'max_pso_duration': """maximum duration of a post-saccadic oscillation
    (glissade) candidate (in seconds)""",
    'max_vel': """maximum velocity threshold, will replace value with
    maximum, and issue warning if exceeded to inform about potentially
    inappropriate filter settings""",
    'median_filter_length': """smoothing median-filter size (for initial
    data chunking only) (in seconds)""",
    'min_blink_duration': """missing data windows shorter than this
    duration will not be considered for --dilate-nan (in seconds)""",
    'min_fixation_duration': """minimum duration of a fixation event
    candidate (in seconds)""",
    'min_intersaccade_duration': """no saccade detection is performed in
    windows shorter than twice this value, plus minimum saccade and PSO
    duration (in seconds)""",
    'min_pursuit_duration': """minimum duration of a pursuit event
    candidate (in seconds)""",
    'min_saccade_duration': """minimum duration of a saccade event
    candidate (in seconds)""",
    'noise_factor': """adaptive saccade onset threshold velocity is the
    median absolute deviation of velocities in the window of interest,
    times this factor (peak velocity threshold is twice the onset velocity);
    increase for noisy data to reduce false positives""",
    'pursuit_velthresh': """fixed drift velocity threshold to distinguish
    periods of pursuit from periods of fixation; higher than natural ocular
    drift velocities during fixations""",
    'saccade_context_window_length': """size of a window centered on any
    velocity peak for adaptive determination of saccade velocity thresholds
    (for initial data chunking only) (in seconds)""",
    'savgol_length': """size of Savitzky-Golay filter for noise reduction
    (in seconds)""",
    'savgol_polyord': """polynomial order of Savitzky-Golay filter for noise
    reduction""",
    'velthresh_startvelocity': """start value for adaptive velocity threshold
    algorithm, should be larger than any conceivable minimum saccade velocity
    (in deg/s)""",
}


def perform_remodnav(x, y,
                     sampling_rate,
                     screen_width,
                     screen_width_pixels,
                     screen_distance,
                     pursuit_velthresh=2.0,
                     noise_factor=5.0,
                     velthresh_startvelocity=300.0,
                     min_intersaccade_duration=0.04,
                     min_saccade_duration=0.01,
                     max_initial_saccade_freq=2.0,
                     saccade_context_window_length=1.0,
                     max_pso_duration=0.04,
                     min_fixation_duration=0.04,
                     min_pursuit_duration=0.04,
                     lowpass_cutoff_freq=4.0,
                     min_blink_duration=0.02,
                     dilate_nan=0.01,
                     median_filter_length=0.05,
                     savgol_length=0.019,
                     savgol_polyord=2,
                     max_vel=3000.0):

    px2deg = deg_per_pixel(screen_width, screen_distance, screen_width_pixels)

    data = np.rec.fromarrays([x, y], names=['x', 'y'])
    lgr.info('Read %i samples', len(data))

    clf = EyeGazeClassifier(px2deg, sampling_rate, pursuit_velthresh, noise_factor, velthresh_startvelocity,
                            min_intersaccade_duration, min_saccade_duration, max_initial_saccade_freq,
                            saccade_context_window_length, max_pso_duration, min_fixation_duration,
                            min_pursuit_duration, lowpass_cutoff_freq)

    pp = clf.preproc(data, min_blink_duration, dilate_nan, median_filter_length, savgol_length,
                     savgol_polyord, max_vel)

    events = clf(pp, classify_isp=True, sort_events=True)

    return events, pp, clf
