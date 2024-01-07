<p align="center">
<img src="../image/keys.png" style="float;" width="500" height="250">
</p>

User requests follow a Zipfian distribution. This observation signifies that specific segments of the data experience a higher volume of requests, a pattern that evolves over
time. To mimic user behavior accurately, we proceeded to
generate 5 million requests using a Zipfian distribution with
a α= 0.9. As illustrated, the distributions of keys for normal and bots. As can be seen, there are more request for some part of data (i.e., popular/hot items) and less request for some other (i.e., unpopular/cold items). However, as shows, cold items for normal users consider as hot items for bots.


1. Generating zipfian keys (normal_requests_5m.csv):
```bash
gcc zipfian.c -o zipfian -lm
./zipfian
```

2. Generating moderate:
```bash
python generate_moderate.py
```
You can repeat the same for generaing other bot type.

3. Computing histogram based on bins:
```bash
gcc compute_histogram.c -o compute_histogram
./compute_histogram
```

4. Generating abnormal requests (anormal_requests_5m.csv):
```bash
gcc generate_abnormal.c -o generate_abnormal
./generate_abnormal
```

4. Plotting the histogram:
```bash
python plot.py
```



