# Introduction

syemte is a simple (yet effective) multitrack editor using rubberband (pitch-shifting) + pydub.

# Dependencies

 - [Python 3](https://www.python.org/)
   - [pydub](http://pydub.com/)
 - [rubberband](http://breakfastquay.com/rubberband/)
   - [ffmpeg](http://ffmpeg.org/) (optional)

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

# Demo

```
$ ./syemte/sampler.py
$ for i in ./example/track*.py; do "$i"; done
$ ./example/merge.py
```
