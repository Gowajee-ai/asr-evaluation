# Gowajee ASR Evaluation

## Pre-requisition
- Python 3 (recommend 3.10.x)
- Pip
- Ground Thruth (Reference)
- Transcript (The results from Gowajee)

## Install
```
pip install -r requirements.txt
```

## Usage
1. Create ground-thruth & transcript text files in `/test_set`
example:
```
    test_set
    │   ground_truth_1.txt
    │   transcript_1.txt
    │   ground_truth_2.txt
    │   transcript_2.txt
    ...
    └───
```
2. Fix `config.json` test set file path to path of your ground-thruth & transcript text files
example:
```json
{
  "test_set": [
    {
      "transcript": "./test_set/transcript_1.txt",
      "ground_truth": "./test_set/ground_truth_1.txt"
    },
    {
      "transcript": "./test_set/transcript_2.txt",
      "ground_truth": "./test_set/ground_truth_2.txt"
    }
  ]
}
```

3. Run evaluation
```sh
python eval.py
```
or (Run with Docker)
```sh
./script.sh
```

And then, evaluation reulst will show in `/results/result.csv`

## Result
- WER = word error rate (lower is better)
- CER = character error rate (lower is better)
