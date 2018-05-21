RNN Lyrics Generator
------

Install
---

You'll need a [musixmatch](https://www.musixmatch.com/) account. The free one is fine for getting enough lyric samples. Paste your API key in lyric_gen.py

Have Python 3 installed, and if you need to, install [requests](http://docs.python-requests.org/en/master/user/install/#pipenv-install-requests) and [tensorflow](https://www.tensorflow.org/install/).

Install [textgenrnn](https://github.com/minimaxir/textgenrnn)

```bash
pip3 install textgenrnn
```

Generate some lyrics!
---

```bash
python3 lyric_gen.py bob dylan
```

This pulls some lyrics from musixmatch and puts it in `bob_dylan.txt` in the `/lyrics` directory. Then it will generate a 16 line song and put it in `bob_dylan.txt` in the `/output` directory. If you run the command again, it will use the already existing lyrics to generate a new song. 
