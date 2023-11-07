import json
import csv
from jiwer import wer, cer
from pythainlp.tokenize import word_tokenize


def tokenize(text: str):
    word_tokenized_list = map(
        lambda x: x.strip(), word_tokenize(text, engine="deepcut"))
    arr_words = list(filter(lambda x: x != "" and x !=
                     " " and x != "\n", word_tokenized_list))
    joined_words = " ".join(arr_words)
    return joined_words


res = []

with open('./config.json') as c:
    config = json.load(c)
    for test in config['test_set']:
        reference = tokenize(open(test['ground_truth'], "r").read())
        hypothesis = tokenize(open(test['transcript'], "r").read())

        err_wer = wer(reference, hypothesis)
        err_cer = cer(reference, hypothesis)

        print("WER:", err_wer)
        print("CER:", err_cer)
        res.append(
            (
                test['transcript'],
                test['ground_truth'],
                err_wer * 100,
                err_cer * 100
            )
        )

with open("./results/result.csv", "wt") as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerow(["transcript", "ground_truth", "WER (%)", "CER (%)"])
    writer.writerows(res)
