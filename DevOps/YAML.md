# YAML

**Full Form** - Yet Another Markup Language, YAML ain't Markup Language  

1. YAML is a data format used to exchange data 
2. Similar to XML and JSON
3. Simple human readable language to show data
4. In YAML you store only data, not commands 

**Data Serializaion** - The process of conversion of data object into a stream of storage (storage could be db, json, yaml). Deserialization is the opposite of it.  

Data Serialization Languages - YAML, JSON, XML.  

YAML is used in configuration files. It also used in logs, caches, etc.  
YAML has strict syntax. Indentation is important. It can be easily converted to JSON. It is powerful in representing complex data.  

**Extension** - .yaml, .yml  

1. You can store key data pairs in YAML.  
2. YAML is case sensitive.  
3. Indentation is done with spaces in YAML and indentation is very important.  
4. YAML doesnt have multi line comments

## Data Types
There are various datatypes in YAML. They are -  
1. String - can be represented with no quotes, "" or ''
2. Integer
3. Float
4. Boolean
5. Key Values
6. Pairs
7. Sets
8. Dictionary

If some keys of a sequence are empty, this is called a sparse sequence.  
Key : Value pairs are maps in YAML.  
Keys may have duplicate values, these are called pairs.

**Anchors** - We can use anchors to reuse a set of variables.  
*Make Anchor* - `&<anchor_name>`  
*Use Anchor* - `<<: *<anchor_name>`  
You can override anchors by creating the same attribute below with different value.  


