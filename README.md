# How to use #

## Project Setup ##

>- Install Python3 by this link: <https://www.python.org/ftp/python/3.5.2/python-3.5.2-amd64.exe>.
>- Set up Python directory, and Python/Script in System __PATH__ directory (if you are on windows).
>- Install pip by following instruction of this link: <https://pip.pypa.io/en/stable/installing/>.
>- Install packages listed in __requirement.txt__.

## Get Comments ##

>- Find the product ID, for example, given a link <https://item.jd.com/54764005930.html>, and we can see __54764005930__ is the product ID.
>- Change the hyper parameter: _data_expect_to_retrieve_ and _coold_down_time_.
>- Run the script by typing following command __in your script locaiton directory__

``` cmd
python jd_comments_retrive.py
```

| parameter               | explain                                                    |
| ----------------------- | ---------------------------------------------------------- |
| data_expect_to_retrieve | the comments we expected to retrieve from the product page |
| cool_down_time          | the time we delay for each request (10 items per-batch)    |

- I haven't test and don't know what will happen the request amount exceed existed comments on the page, it should be OK, but you can always set a smaller retrieve data amount to keep it cool.
- Try to set up a longer cool down time, so that it won't overshoot the server, and the server may shutdown and ignore the request (I haven't experience myself in my code, but it is a common sense that server have a protection mode)

A file should be able to geneated in the your python location directory: such like __54764005930_comments.jd__ in the sample.

## Generate the Word Cloud ##

>- Assign data source, by assigning the variable ___file_to_process__ in script __word_cloud_generator.py__ as the __.jd__ file created previously.
>- Optional, you can assign the font you want to use in word cloud that created, must be the font file absolute path
>- Set the words you are not interested in the word cloud in list variable ___ignore_words___.
>- Run the script by typing following command __in your script locaiton directory__

``` cmd
python word_cloud_generator.py
```
