% Usage: Automatically filters data and uses ICA to reject bad components.
%        
% ------------------------------------------------

addpath("eeg_lab\")

%Env variables
PATH_IN = './data/tmp/eeg_raw'; % The folder where the files to convert are.
PATH_OUT = './data/tmp/ica'; % The output folder.
files = dir(fullfile(PATH_IN, "*.vhdr"));
files = arrayfun(@(data){data.name}, files);
convert_files(PATH_IN, files, PATH_OUT)

function convert_files(PATH_IN, files, PATH_OUT)
    for file = transpose(files)
        convert_file(PATH_IN, string(file), PATH_OUT);
    end
end

function convert_file(PATH_IN, file_name, PATH_OUT)
    % Load the first data set. Needs to be VDHR. 
    [ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
    EEG = pop_loadbv(PATH_IN, file_name);
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, 0,'setname','15_R1','gui','off');

    % Apply filters TODO this is currently still notch 2,200
    EEG = pop_eegfiltnew(EEG, 'locutoff', 4, 'hicutoff', 200, 'plotfreqz', 1);
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, 1,'gui','off');
    EEG = eeg_checkset( EEG );
    EEG = pop_eegfiltnew(EEG, 'locutoff',49,'hicutoff',51,'revfilt',1,'plotfreqz',1);
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, 1,'gui','off');
    EEG = eeg_checkset( EEG );

    % Set channel locs by teheir given name
    % TODO check if this is correct
    EEG=pop_chanedit(EEG, 'lookup','./data/EEG/standard_1020.elc');
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = eeg_checkset( EEG );

    % Compute ICA
    % Note, currently sobi is selcted here because it is faster then
    % runica. Should probably investigate if that makes a big difference.
    EEG = pop_runica(EEG, 'icatype', 'sobi');
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = eeg_checkset( EEG );

    % Label ICA components
    EEG = pop_iclabel(EEG, 'default');
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = eeg_checkset( EEG );

    % Flag ICA components
    % The flags for this are stored in EEG.reject.gcompreject
    % See https://github.com/sccn/ICLabel/blob/master/pop_icflag.m
    EEG = pop_icflag(EEG, [NaN NaN;0.9 1;0.9 1;NaN NaN;NaN NaN;NaN NaN;0.95 1]);
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = eeg_checkset( EEG ); % ok so checkset checks for the consitency of the data. Is this necessaray though given that everything is automated?
    
    % Reject ICA copmonents
    range = [1:size(EEG.reject.gcompreject)];
    rejects = range(EEG.reject.gcompreject(:,end) == 1);
    EEG = pop_subcomp( EEG, rejects);
    
    % Save the data set
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, 2,'gui','off');
    EEG = eeg_checkset( EEG );
    [p,f,e] = fileparts(file_name); % Get filename without extension or path.
    new_file_name = convertStringsToChars(strcat(f, ".set"));
    EEG = pop_saveset( EEG, new_file_name,PATH_OUT);
    eeglab redraw;
end