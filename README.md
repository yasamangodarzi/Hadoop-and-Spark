# Hadoop and Spark Cluster Project

This project is part of the Kubernetes course's final phase, focusing on working with Hadoop and Spark clusters for distributed storage and parallel processing.

## Project Overview
In this project, we set up and utilized a Hadoop cluster for distributed file storage and a Spark cluster for distributed and parallel file processing using Docker Compose. A Jupyter notebook is also provided for direct code execution.

### **Cluster Setup Steps:**

1. **Clone the repository:**
   ```bash
   git clone git@github.com:sadegh-msm/hind.git
   ```
   For ARM64 architecture:
   ```bash
   git clone -b arm64 git@github.com:sadegh-msm/hind.git
   ```

2. **Build the master node:**
   ```bash
   bash master-build.sh
   ```

3. **To delete the cluster:**
   ```bash
   bash master-delete.sh
   ```

### **Access the Cluster Interfaces:**
- **Hadoop UI:** [http://localhost:9870](http://localhost:9870)
- **Spark Master UI:** [http://localhost:8080](http://localhost:8080)
- **Jupyter Notebook:** [http://localhost:8888](http://localhost:8888)

---

## **MapReduce Implementation Steps:**

1. **Complete Mapper and Reducer Scripts in Python:**
   - **Mapper Script:**
     - Input: Document ID and document text.
     - Process: Generates a unique pair of word and document ID for each word.
   - **Reducer Script:**
     - Input: Word and list of document IDs.
     - Process: Calculates unique document IDs for each word and outputs them.

2. **Transfer scripts to NameNode:**
   - Upload `mapper.py` and `reducer.py` to the NameNode.

3. **Prepare Data in HDFS:**
   - Upload the input data from `input.txt` to HDFS using `hdfs` commands.

4. **Run MapReduce Job with Hadoop Streaming:**
   ```bash
   hadoop jar /opt/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input input/input.txt -output output
   ```
   Note: Since Hadoop is built on Java, it requires a JAR file. Hadoop Streaming allows running Python code by processing input from STDIN.

5. **Check the Output:**
   - View the output files in the `output` directory after the job completes.



