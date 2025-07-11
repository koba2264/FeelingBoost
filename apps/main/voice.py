import requests

def tts_and_play(text, speaker=1, out_path="output.wav"):
    host = "http://127.0.0.1:50021"
    r = requests.post(f"{host}/audio_query", params={"text": text, "speaker": speaker})
    r.raise_for_status()
    audio_query = r.json()
    r = requests.post(f"{host}/synthesis", params={"speaker": speaker}, json=audio_query)
    r.raise_for_status()
    wav_data = r.content
    with open(out_path, "wb") as f:
        f.write(wav_data)
    print(f"保存完了: {out_path}")
