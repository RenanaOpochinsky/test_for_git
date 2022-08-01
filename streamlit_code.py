import os
import streamlit as st
import glob
#from typing_extensions import TypeGuard

st.title("Model Compare")
# st.set_page_config(layout="wide")

model_path = "/dsi/gannot-lab/datasets/mordehay/Result/Test"
models = os.listdir(model_path)

col1, col2 = st.columns(2)
with col1:
    selected_model = st.selectbox("Select model 1", models)
    eval_files = glob.glob(f'{model_path}/{selected_model}/Batch_*')

    scenarios = {}
    for i, files_dir in enumerate(eval_files):
        scenario_dir = os.path.dirname(files_dir)
        scenario = files_dir.split(os.sep)[-1]

        if not os.path.exists(files_dir):
            continue

       # separate scenario name
        sisdri = scenario.split('_')[3]
        rt60 = scenario.split('_')[5]
        snr = scenario.split('_')[7]

        mix_file = os.path.join(files_dir, 'mixed.wav')
        output0_file = os.path.join(files_dir, 'output_0.wav')
        ref0_file = os.path.join(files_dir, 'clean_0.wav')

        if os.path.exists(os.path.join(files_dir, 'output_1.wav')):
            output1_file = os.path.join(files_dir, 'output_1.wav')
            ref1_file = os.path.join(files_dir, 'clean_1.wav')

            scenarios[scenario] = [sisdri, rt60, snr, mix_file, output0_file, output1_file, ref0_file, ref1_file]

        else:
            scenarios[scenario] = [sisdri, mix_file, output0_file]

    sorted_scenarios = {k: v for k, v in sorted(scenarios.items(), key=lambda item: item[0])}

    selected_scenario = st.selectbox("Select scenario 1", sorted_scenarios)

    scene = sorted_scenarios[selected_scenario]


    st.text('sisdri =')
    st.write(scene[0])
    st.text('rt60 =')
    st.write(scene[1])
    st.text('snr =')
    st.write(scene[2])
    st.text('mixture signal:')
    st.audio(scene[3])
    st.text('output1 signal:')
    st.audio(scene[4])
    st.text('output2 signal:')
    st.audio(scene[5])
    st.text('ref1 signal:')
    st.audio(scene[6])
    st.text('ref2 signal:')
    st.audio(scene[7])


with col2:
    selected_model2 = st.selectbox("Select model 2", models)
    eval_files2 = glob.glob(f'{model_path}/{selected_model2}/Batch_*')

    scenarios2 = {}
    for i, files_dir2 in enumerate(eval_files2):
        scenario_dir2 = os.path.dirname(files_dir2)
        scenario2 = files_dir2.split(os.sep)[-1]

        if not os.path.exists(files_dir2):
            continue

       # separate scenario name
        sisdri2 = scenario2.split('_')[3]
        rt602 = scenario2.split('_')[5]
        snr2 = scenario2.split('_')[7]

        mix_file2 = os.path.join(files_dir2, 'mixed.wav')
        output0_file2 = os.path.join(files_dir2, 'output_0.wav')
        ref0_file2 = os.path.join(files_dir2, 'clean_0.wav')

        if os.path.exists(os.path.join(files_dir2, 'output_1.wav')):
            output1_file2 = os.path.join(files_dir2, 'output_1.wav')
            ref1_file2 = os.path.join(files_dir2, 'clean_1.wav')

            scenarios2[scenario2] = [sisdri2, rt602, snr2, mix_file2, output0_file2, output1_file2, ref0_file2, ref1_file2]

        else:
            scenarios2[scenario2] = [sisdri, mix_file, output0_file]

    sorted_scenarios2 = {k: v for k, v in sorted(scenarios2.items(), key=lambda item: item[0])}

    selected_scenario2 = st.selectbox("Select scenario 2", sorted_scenarios2)

    scene2 = sorted_scenarios2[selected_scenario2]

    st.text('sisdri =')
    st.write(scene2[0])
    st.text('rt60 =')
    st.write(scene2[1])
    st.text('snr =')
    st.write(scene2[2])
    st.text('mixture signal:')
    st.audio(scene2[3])
    st.text('output1 signal:')
    st.audio(scene2[4])
    st.text('output2 signal:')
    st.audio(scene2[5])
    st.text('ref1 signal:')
    st.audio(scene[6])
    st.text('ref2 signal:')
    st.audio(scene2[7])
    #eval_files = glob.glob(f'{model_path}/{selected_model}/checkpoints/lightning_logs/*///.rxt')
