############################################
# The statistic figure for the NGG detection
# By Zongrui Dai: dzr17723980497@gmail.com
############################################
library(ggplot2)
library(reshape2)
setwd('D:/test')
d<-read.csv('NGG.csv')
chr19<-d[1:19,]
ID<-c('chr1','chr2','chr3','chr4','chr5','chr6',
      'chr7','chr8','chr9','chr10','chr11','chr12',
      'chr13','chr14','chr15','chr16','chr17','chr18',
      'chr19')
chr19$ID<-as.factor(ID)
c<-melt(chr19[,-c(2,7)])

ggplot(c,aes(x=ID,y=value))+
  geom_bar(stat = 'identity',aes(fill = variable),width = 0.9) +
  theme(text=element_text(family="Songti SC",size=12,face = "bold"), #设置文字的字体字号（设置字体是为了确保汉字可以显示，字号和加粗请随意）
        axis.text.x = element_text(size=10,angle=45))+
  ggtitle('The frequency of NGG')

chr19$per<-chr19$Sum/chr19$Length
chr19$ID<-as.factor(chr19$ID)
ggplot(chr19,aes(x=ID,y=per))+
  geom_bar(stat = 'identity',aes(fill = ID),width = 0.9) +
  theme(text=element_text(family="Songti SC",size=12,face = "bold"), #设置文字的字体字号（设置字体是为了确保汉字可以显示，字号和加粗请随意）
        axis.text.x = element_text(size=10,angle=45))+
  ylim(0,0.05)+ggtitle('The percentage of NGG')



