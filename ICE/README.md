# ICE

ICE is an Integrated Customization Environment for Information Extraction developed by Yifan He and Ralph Grishman at NYU. More information can be found at the website http://nlp.cs.nyu.edu/ice/. You can also download the original software at their website.

## Set up ICE

### Install X Server
Since ICE is GUI-based, you will need an X server to run it remotely. Please google "xserver + your operating system" to find out how to set it up. You can test whether the setup is successful by running the following commands:
```
ssh -X username@address
xclock
```
If successful, you should see a display of a clock on your local machine. The `-X` flag can be replaced by `-Y`.

### Set up the original version

Download the original software from [here](https://github.com/ivanhe/ice/releases/download/v0.2.0beta/ice-bin.zip "ice-bin.zip") (I copied the link from ICE's website). Then unzip the file and under the directory `ice-bin/`, exsecute the following command to run the software:
```
./runice.sh
```

### Set up the pre-trained version

The [ice-bin](./ice-bin) folder here contains the contents of ICE after I trained it on a corpus of 4000 legal documents, except the cache for the preprocessed documents.

The folder can also be found on the CIMS server at `/misc/proteus106/wlu/ice-bin`.

The corpus can be found at `/misc/proteus106/wlu/legal_corpus/4000/texts/`.

To run the software, download the [ice-bin](./ice-bin) folder to a CIMS server. When running it for the first time, direct to `ice-bin/` and run the following command to add the cache of the preprocessed corpus:
```
cp -r /misc/proteus106/wlu/ice-bin/cache cache
```
Then, execute the following command to run the software:
```
./runice.sh
```

## Use ICE

This [video](https://www.youtube.com/watch?v=7r53EpTy1_M) has a fairly clear demo of how to use the software. Also, under [ice-bin/docs/](./ice-bin/docs), you can find the file [iceman.html](./ice-bin/docs/iceman.html), which contains some more details that are not in the video. 

In the end, the entity set and relation set that you build through ICE will be exported as two files. They can be found under [ice-bin/acedata/](./ice-bin/acedata), where [ice_onoma.dict](./ice-bin/acedata/ice_onoma.dict) is the file for entity set, and [iceRelationModel](./ice-bin/acedata/iceRelationModel) is the file for relation set.

# Jet

The outputs of ICE are going to be used by JET, the Java Extraction Toolkit, which is a set of language analysis tools developed by Ralph Grishman. More information on JET can be found at http://cs.nyu.edu/grishman/jet/guide/Jet.html.

## Set up JET

ICE already contains the files for JET so you don't need to download additional files. You will only need to add the following lines to your bash profile:

```
export PATH=$PATH:/misc/proteus106/wlu/ice-bin/bin
export JET_HOME="/misc/proteus106/wlu/ice-bin"
```

## Use JET

The actions of JET is controled by a properties file. The [props2](./ice-bin/props2) under [ice-bin/](./ice-bin) will ask JET to take the outputs of ICE and perform named entity recognition and relation extraction on target documents.

You can use the `ace` command to run JET. It takes in four arguments:
1. Path to the properties file
2. Path to the file that contains the filenames of the documents to be processed
3. Path to the directory that contains the files to be processed
4. Path to the the output directory
[runAceIce](./ice-bin/runAceIce) under [ice-bin/](./ice-bin) contains a simple script that shows the usage.
