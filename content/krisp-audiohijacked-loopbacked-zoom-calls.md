Title: Krisp Audio Hijacked Loopbacked Zoom Calls
Slug: krisp-audiohijacked-loopbacked-zoom-calls
Author: Eoin Brazil
Date: 2020-11-09
Category: Blog/HomeOffice
Tags: office, software, hardware

I wanted to write up a short post around the audio setup I am using for my day-to-day Zoom Calls. It might be helpful to others and it's really given my audio setup a lift. 

This post covers the specific details that [my earlier post didn't](http://eoinbrazil.com/home-office-bill-of-materials.html) as I wanted to expand on my use of [Krisp](https://krisp.ai/) and how everything is setup for [Zoom](https://zoom.us/). These details will allow anyone reading to replicate this configuration for their own conference calls.

#### Audio Hardware

I use a [Rode Podcaster USB Broadcast Microphone](http://www.rode.com/microphones/podcaster), a [PSA1 Studio Boom Arm](http://www.rode.com/accessories/psa1) and [SMR Advanced Shock Mount](http://www.rode.com/accessories/smr) for my audio hardware for calls.

#### Audio Software

I am a huge fan of all things [Rogue Amoeba](https://rogueamoeba.com/), they simply make great software.

In [Zoom](https://zoom.us/) I use the advanced audio configuration to enable the original audio input and remove echo cancellation as well as to select a higher quality of audio. These settings are really important as otherwise all the later audio processing won't really add much quality or value to your audio for other call participants. In most calls, you will still have to manually select use original audio and hopefully down the line that will be might also be a default setting.

![Zoom setup]({attach}extras/zoom_advanced_audio_setup.png)

For [Zoom](https://zoom.us/), I use firstly use [Krisp](https://krisp.ai/) and I pipe my microphone to it as an input. It uses Deep Neural Networks to provide noise cancellation. It has 'learnt' many different noises and fairly seamlessly removes these from the audio input.

I think use [Audio Hijack](https://rogueamoeba.com/audiohijack/) to further process the audio output from [Krisp](https://krisp.ai/). I use the following processing elements: Declick, Dehum, AUHighShelfFilter, AUPeakLimiter, and AUMultiBandCompressor. This is then sent to a ZoomOutputDevice from within the application.

![AudioHijack setup]({attach}extras/audio_hijack_zoom_setup.png)

Finally, I use [Loopback](https://rogueamoeba.com/loopback/) for wiring my Audio Hijack output to [Zoom](https://zoom.us/) and to also link [Farrango](https://rogueamoeba.com/farrago/) to [Zoom](https://zoom.us/). I find that [Farrango](https://rogueamoeba.com/farrago/) is great as a sound board with a few extra sounds from [FreeSound.org](https://freesound.org/) to add precanned sound effects to any call.

![Loopback setup]({attach}extras/loopback_setup_zoom.png)
