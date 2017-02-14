# Welcome to Lbppy (pronounced "Lippy")

This is a Python library designed to facilitate the consumption of the data from the SCTA Database and API [http://scta.info](http://scta.info)

It shares a basic design architecture with the parallel ruby gem [lbp.rb](http://github.com/lombardpress.rb)

# Example

Imagine that you have written a python program that compares and automatically collates parallel text transcriptions.

The "Lbppy" library can you help you easily and quickly generalize that program to work on all texts within the SCTA catalogue at any level, without knowing how many transcriptions of a text exist or even where they are on the web.

All you need is the Expression ID of the text in question and everything else can be one for you.

For example, you might be interested in comparing transcriptions of Lecture 1 of Peter Plaoul's Commentary on the Sentences of Peter Lombard.

The Expression ID for lecture 1 is `http://scta.info/resource/lectio1`

After importing the `lbppy` library like so:

`import lbppy`

You can load the resource:

```
resource = lbppy.Resource.find("http://scta.info/resource/lectio1")

```

Because the resource in question is an Expression, the `resource` object will be returned as an instance of the Expression class along with a number of available Expression level methods. Using the `manifestations()` method, we can retrieve all the ResourceIdentifiers of known Manifestations like so:

```
manifestations = resource.manifestations()
```

From here, by calling the method `resource()` we can get an instance of the Manifestation Class, and then use the Manifestation level methods to as ask for the canonical or default transcription of each manifestation, like so:

```
transcriptions = []
for m = manifestations:
  transcriptions[] = m.resource().canonical_transcription()
```

It's likely that a collation program will want to use an XSLT script to convert the raw xml to plaintext so that the collation can be preformed. The `lbppy` library can assist in both the retrieval of these xml documents from distributed locations on the web and their conversion. This might be written as follows:

```
plaintexts = []
for t in transcriptions:
  plaintexts = t.resource().file().transform("https://raw.githubusercontent.com/lombardpress/lombardpress-web/develop/xslt/1.0.0/critical/main_view.xsl")
```

Simply supply an XSLT file and the conversion will be completed.

Now, without requiring any prior knowledge of the text and its related parts and locations, you immediately have a list of plaintext files that can be compared in the original collation program.

To perform the collation, on another text, simply supply a new Expression ID.

# Contributors

* [Jeffrey C. Witt](http://jeffreycwitt.com)
