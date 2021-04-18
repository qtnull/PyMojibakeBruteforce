# Mojibake Brute-force recovery tool written in Python 3
A quick and dirty brute-force tool for recovering Mojibake

# What is Mojibake?

A mojibake is a text encoded in a encoding scheme, but decoded and displayed to user with a different encoding scheme than the original.
It creates a garbled text that cannot be read by the user.

For example:
`文字化け` (Translation: mojibake) encoded in EUC_JP
EUC_JP read as ISO-8859-1: `Ê¸»ú²½¤±`

For more information, please visit this [Wikipedia article](https://en.wikipedia.org/wiki/Mojibake)

# How does it work?

To untangle a mojibake, first we need to know 2 things:

1. Mojibake's encoding
2. Original text's encoding

After we know those 2 things, we can start untangling them. First, we must get the original hex of the Mojibake, this is achieved by encoding the Mojibake again with the Mojibake's encoding scheme. Python conveniently has an encode function build into every `string` instance (called `string_instance.encode(encoding)`, or `bytes(str, encoding)`, which returns a `bytes` object)

For example: we know that this garbled text `Ê¸»ú²½¤±` is ISO-8859-1, we can obtain the original hex data by encoding the garbled text with ISO-8859-1, and it gives us this:

```
>>> "Ê¸»ú²½¤±".encode("ISO-8859-1")
b'\xca\xb8\xbb\xfa\xb2\xbd\xa4\xb1'
```

Translated to human "readable" hex is: `0xCA 0xB8 0xBB 0xFA 0xB2 0xBD 0xA4 0xB1`

Now we need to know the original text's encoding, if we know this, we can just decode the hex with the original text's encoding scheme. Again, python also conveniently provides a decode function to every instance of `bytes` (don't tell me you don't know hex in a `bytes` object in python, anyway, use `bytes_instance.decode(encoding)` or `str(bytes, encoding)`)

For example, in the previous example, we know it's EUC_JP, so we can just decode the hex with EUC_JP and call it a day.

```
>>> b'\xca\xb8\xbb\xfa\xb2\xbd\xa4\xb1'.decode("euc_jp")
文字化け
```

# Okay? Then how can you know the text's encoding in real life scenarios?

Well... Chances are... you don't, that's why this tool is developed, this tools tries every encoding scheme possible (provided by the Standard Codecs table by Python 3.9) and decode it with the encoding scheme that you provided. You must guess the original text's encoding scheme. You also have to know what the text's language is, if not, you won't be able to tell the difference between mojibake and the actual text, just like Korean encoded in SHIFT_JIS (?) and you don't know Korean and Japanese, at least you have to know how to tell the difference.

This program's job is to brute-force the Mojibake's encoding. Although the opposite can be done too, you know the mojibake's encoding scheme and this program brute-forces the original text's encoding, but I'm too lazy to implement that, feel free to create a pull request.

## Why don't you brute-force both the original and mojibake's encoding scheme?
Python supports 97 encoding schemes, which brings us to an interesting question, recovering a Mojibake requires the user to check if the produced results makes sense or not. And sifting through 97*97 results is just... Unbelievable. Sure, Python will throw exceptions on 70% of the recovery tries, but it's still a gigantic number of results.

# How do I use it?

`py bruteforce_encoding.py [encoding] [message]`

Parameters:

`encoding`: target encoding scheme, in other words: the message's original encoding scheme (you must guess it)

`message`: message to bruteforce (Tip: use quotation marks, some mojibakes have a space character in them, and causes the program to not recognize the parameters correctly)

The arrow in the output (-->) means 'reencoded as'

## Commandline is $h!t and I don't support it

Neither do I. If you hate it, feel free to learn Python and TKinter and create a pull request. ~~Or rewrite the whole damn thing~~

# FAQ Section
## Why?
Because I play kapanese games and my system language is set to Chinese, creating Mojibake very often while playing ~~japanese visual novels~~ japanese games.
## Your code looks awful
Thanks, please send your critiques to thebuster000 *at* gmail *dot* com, or create issues. I'm still learning Python and C#, recommendations and critiques would be awesome.
## You don't even know what you are talking about! You don't know how to explain!
I only know *how to use* those functions, not *how they work* under the hood, explaining everything would be a big hassle, the above explanation is more or less an oversimplified version of the Wikipedia article, and limited by my English level, I apologize for my poor English.
## Miscellaneous
Visual novel? Karenai Sekai to Owaru Hana

Anime? Non Non Biyori

Hotel? Trivago
