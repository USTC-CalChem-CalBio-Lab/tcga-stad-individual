各代码作用：

gdc_scan.py
从tcga-portal获取所需信息。
用法：在控制台输入
python(3.6) gdc_scan.py files download --format MAF --project TCGA-PAAD(TCGA上的癌症类型)

tcga-stad.py
从网页上抓取胃癌四种分类数据（2013年版）。
输出:./tcga-stad/type.csv

extract.py
将从网页上提取的四组不同类型的胃癌从maf文件中分离。
输入:mutect.maf
输出:./data/type/sample.maf



maf2vcf.pl
将从tcga-portal得到的maf数据转化为vcf文件。
用法：在控制台输入 
perl vcf2maf.pl --input-vcf [input-maf] --output-dir [output-vcf]
PS:	需要依赖文件进行注释，文件名在第12行，按需修改路径。
	文件直接google搜索 Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa 下载第一个即可，需要GRCh37直接将文件中38替换为37搜索第一个下载即可。
	第105行可以调整一次读入的行数，
错误及解决：	①Your MAF uses CR line breaks, which we can't support. Please use LF 				or CRLF.
			解决：在控制台输入
					perl -lne 's/\r//; print "$_";' input-file output-file
			②

2vcf.sh
shell脚本调用maf2vcf。
用法：在控制台输入 ./2vcf.sh

