import os
import mne
from pybv import write_brainvision
import numpy as np
import pybv

path_to_raw_files: str = "./data/rawData"
filepath_out: str = "./data/eeg_tmp/raw"
montage_path = "AC-64.bvef"
channels_to_drop = ['x_dir', 'y_dir', 'z_dir']


def load_fif_file(filename, filepath):
    print('Loading record \'' + filename + '\' from ' + filepath)
    full_filename = os.path.join(filepath, filename)
    return mne.io.read_raw_fif(fname=full_filename + '.fif', preload=True)


def convert_fif_to_set(filename, load_from, save_to):
    raw = load_fif_file(filename, load_from)

    # set montage
    montage = mne.channels.read_custom_montage(montage_path, head_size=0.085)
    # montage.plot()
    raw.set_montage(montage)

    # drop channels
    raw.drop_channels(channels_to_drop)

    savepath: str = os.path.join(save_to, filename + ".vhdr")
    mne.export.export_raw(savepath, raw, 'eeglab', 'auto', overwrite=True)
    events = raw.info["events"]
    np_e = []
    for e in events:
        np_e.append([e['list'][0], e['list'][2]])

    np_array = np.asarray(np_e)
    # event_np = (x for x in events)

    channels = raw.ch_names
    # df = raw.to_data_frame()
    df = raw.get_data(channels)
    write_brainvision(data=df, sfreq=500, ch_names=channels, folder_out=filepath_out, fname_base=filename,
                      events=np_array, overwrite=True)


def main():
    from os import listdir

    for f in listdir(path_to_raw_files):
        convert_fif_to_set(os.path.splitext(f)[0], path_to_raw_files, filepath_out)
    print(f"DONE!")


if __name__ == "__main__":
    main()
