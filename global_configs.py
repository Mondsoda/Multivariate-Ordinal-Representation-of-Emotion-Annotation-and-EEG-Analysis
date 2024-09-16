# global
Cls = 9
ES_dim = 8
Fs = 250
RandSeed = 7
N_subs = 30
N_folds = 10
N_vids = 28
N_timeFilters = 16
N_spatialFilters = 16
N_channs = 30
Sec = 30
TimeFilterLen = 60
Temperature = 0.07
MultiFact = 2
Ordinal = True
Tolerance = 0
Adjacent = 0
Threshold = [0.5]
N_views = 2
Restart_times = 3 # number of cycles in CosineAnnealingWarmRestarts

# pretrain
Use_emoCLR = True
Batch_size_pretrain = 28
TimeLen_pretrain = 5
Learning_rate_pretrain = 0.0007
Weight_decay_pretrain = 0.015
Epochs_pretrain = 80
TimeStep_pretrain = 2
Max_tol_pretrain = 30
Channel_norm_pretrain = False
Time_norm_pretrain = False
N_times = 1 # number of sampling times for one sub pair (in one session)

# classification
Epochs_finetune = 100
Learning_rate_finetune = 0.0005
TimeLen_classify = 1
TimeStep_classify = 2
Batch_size_finetune = 270
Weight_decay_finetune = 0.05
Max_tol = 50
Val_method = 'N_folds'
Hidden_dim = 30
FiltLen = 1
Channel_norm_classify = True
Time_norm_classify = False
Stratified = False
IsFilt = False

Selected_bands = [[0.5,3], [4,7], [8,13], [14,29], [30,47]]

def format_float(float_number):
    """
    The format_float function takes a floating-point number as input and returns a string representation
    of the number without trailing zeros or an unnecessary decimal point. If the number is an integer,
    it will be returned without any decimal point.
    """
    float_str = str(float_number)
    formatted_str = float_str.rstrip('0').rstrip('.') if '.' in float_str else float_str

    return formatted_str
# paths
Root_dir = '.'
To_After_remarks = '../After_remarks'
To_log_dir_24 = './runs_srt_ordinal%d/T%sA%dthr%d_%dsubs%dfolds%dcls_24video_batch%d_timeLen%d_tf%d_sf%d_multiFact%d_lr%f_wd%f_epochs%d_randSeed%d'%(
int(Ordinal), format_float(Tolerance), Adjacent, Threshold[0], N_subs, N_folds, Cls, Batch_size_pretrain,  TimeLen_pretrain, N_timeFilters, N_spatialFilters,
        MultiFact, Learning_rate_pretrain, Weight_decay_pretrain, Epochs_pretrain, RandSeed
)
To_log_dir_28 = './runs_srt_ordinal%d/T%sA%dthr%d_%dsubs%dfolds%dcls_28video_batch%d_timeLen%d_tf%d_sf%d_multiFact%d_lr%f_wd%f_epochs%d_randSeed%d'%(
int(Ordinal), format_float(Tolerance), Adjacent, Threshold[0], N_subs, N_folds, Cls, Batch_size_pretrain,  TimeLen_pretrain, N_timeFilters, N_spatialFilters,
        MultiFact, Learning_rate_pretrain, Weight_decay_pretrain, Epochs_pretrain, RandSeed
)
To_Clisa_data = '../Clisa_data'
To_Emotion_matrices = './Emotion_matrices/ordinal%d_tol%s_adj%d'
To_Labels = './Labels/ordinal%d_tol%s_adj%d'
To_Simlarity_matrices = './Simlarity_matrices/ordinal%d_tol%s_adj%d_sub%sto%s_%s'
To_Other_simlarity_matrices = './Simlarity_matrices/%s_first%dsubs'
To_Processed_data = './Processed_data_filter_epoch_0.50_40_manualRemove_ica'

