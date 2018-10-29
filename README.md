###依赖环境安装：

##A MHCnuggets

	pip(3/3.5/3.6/3.7) install MHCnuggets

##B ensembl-vep

	需安装依赖软件

	B1 mysql
		sudo apt-get install mysql-server
		sudo apt install mysql-client
		sudo apt install libmtsqlclinet-dev
		检测：
		sudo netstat -tap | grep mysql

	B2 DBI
		cpan (install) DBI
	
	B3 DBD::mysql
		cpan (install) DBD
		ps:安装过程中提示缺什么就直接cpan (install) 什么 ~~

	安装完成依赖软件之后安装ensembl-vep
	git clone https://github.com/Ensembl/ensembl-vep.git
	(ps:没有安装git请自行安装。。。。。。)
	cd ensembl-vep
	perl INSTALL.pl
	
	ps:	安装时候基本一路选择yes，记得要安装plugins。
		不需要安装fasta，如果根目录剩余空间够大(>10G)可以安装cache，否则手动下载cache。
		手动下载cache方法：
			在ensembl-vep下
			mkdir cache
			cd cache
			curl ftp://ftp.ensembl.org/pub/release-94/variation/VEP/homo_sapiens_vep_94_GRCh38.tar.gz
			tar zxvf homo_sapiens_vep_94_GRCh38.tar.gz

##C pvactools

	pip(3/3.5/3.6/3.7) install pvactools

##D samtools (maf2vcf会用到)
	
	先安装依赖软件

	D1 autoheader
		sudo apt-get install autoheader

	D2 htslib
		git clone https://github.com/samtools/htslib.git
		autoconf
		./configure
		make
		make install

	D3 curses
		apt-get install libncurses5-dev

	安装完成依赖软件之后安装samtools
	git clone https://github.com/samtools/samtools.git
	cd samtools-1.5
	autoheader
	autoconf -Wno-syntax
	./configure --with-htslib=/htslib/install/dir
	


###整体运行流程

##STEP①:利用gdc-scan从gdc-portal提取somatic mutation数据  *.maf

	A1.	搜索指定癌症类型的突变注释格式文件(Mutation Annotation Format, MAF)
		18种癌症癌症类型数据来自 https://portal.gdc.cancer.gov/
	
	A2.	运行gdc_scan.py脚本，其中注意：
			
			A21. 第9行应改为：URL_BASE="https://api.gdc.cancer.gov/"
			A22. 第10行应改为：LEGACY_BASE="https://api.gdc.cancer.gov/legacy/"

	A3.	运行结束后得到压缩包，选择其中 TCGA.STAD.mutect.*.maf 进行解压
		即 tar zxvf TCGA.STAD.mutect.*.maf
	A4.	移动该maf文件至创建的工作目录中，并重命名为mutect.maf
	A5.	mutect.maf文件的前五行需要删除，同时由于染色体表示方式与fasta文件不符，需要删除各条目对应的”chr“,故共有两步操作:
			sed -i '1,5d' mutect.maf //删去前5行
			vim mutect.maf 	//打开文件
			:%s/chr//g 		//正则匹配chr并替换为空字符串
			Enter 			//执行
			:wq				//保存




































