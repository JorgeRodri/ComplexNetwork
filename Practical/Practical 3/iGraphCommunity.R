library(stringr)
library(igraph)


savePartition<- function(net, partitions, name){
  content<- paste('*Vertices ', length(V(net)), '\n', sep='')
  for (node in V(net)){
    for (i in 1:length(partitions)){
      if (node %in% unlist(partitions[i])){
        content<- paste(content, i, '\n', sep='')
        break
      }
    }
  }
  write(content, name)
}



path='C:/Users/jorge/Desktop/MAI/2nd sem/CN/Practical/Practical 3/A3_nets/'
problem.type=c('model/', 'real/', 'toy/')

modularity_walktrap.values<-c()
times_walktrap<-c()
image.folder<-'plots/'

for (folder in problem.type){ 
  loc<-paste(path,folder, sep='')
  files=list.files(loc)
  for (file in files){
    if (grepl('.net', file) & grepl('airports',file)){
      real.file<-paste(loc,file, sep='')
      G <- read_graph(real.file, format =  "pajek")

      start.time <- Sys.time()
      wc <- cluster_walktrap(G)
      end.time <- Sys.time()
      coords = layout_with_fr(G)
      jpeg(paste(image.folder,substr(file,1,nchar(file)-4), '_walktrap.jpg' , sep=''))
      plot(wc, G, layout=coords,vertex.label =' ')
      dev.off()

      time.taken <- end.time - start.time
      times_walktrap<-append(times_walktrap,c(file,round(time.taken,4)))
      modularity_walktrap.values<-append(modularity_walktrap.values,c(file,modularity(wc)))
      print(paste(loc, substr(file,1,nchar(file)-4), '_walktrap.clu' , sep=''))
      savePartition(G,wc,paste(loc, substr(file,1,nchar(file)-4), '_walktrap.clu' , sep=''))
    } else if (grepl('.net', file)){
      real.file<-paste(loc,file, sep='')
      G <- read_graph(real.file, format =  "pajek")
      
      start.time <- Sys.time()
      wc <- cluster_walktrap(G)
      end.time <- Sys.time()
      coords = layout_with_kk(G)
      jpeg(paste(image.folder,substr(file,1,nchar(file)-4), '_walktrap.jpg' , sep=''))
      plot(wc, G, layout=coords,vertex.label =' ')
      dev.off()
      
      time.taken <- end.time - start.time
      times_walktrap<-append(times_walktrap,c(file,round(time.taken,4)))
      savePartition(G,wc,paste(loc, substr(file,1,nchar(file)-4), '_walktrap.clu' , sep=''))
      modularity_walktrap.values<-append(modularity_walktrap.values,c(file,modularity(wc)))
      print(paste(loc, substr(file,1,nchar(file)-4), '_walktrap.clu' , sep=''))
    }
  }
}
B.walktrap = matrix( modularity_walktrap.values , nrow=length(modularity_walktrap.values)/2, ncol=2, byrow=TRUE) 
#####################################
#
#Louvain
#
###################################################

modularity_louvain.values<-c()
times_louvain<-c()

for (folder in problem.type){ 
  loc<-paste(path,folder, sep='')
  files=list.files(loc)
  for (file in files){
    if (grepl('.net', file) & grepl('airports',file)){
      real.file<-paste(loc,file, sep='')
      G <- read_graph(real.file, format =  "pajek")
      start.time <- Sys.time()
      wc <- cluster_louvain(G)
      end.time <- Sys.time()

      coords = layout_with_fr(G)
      jpeg(paste(image.folder,substr(file,1,nchar(file)-4), '_louvain.jpg' , sep=''))
      plot(wc, G, layout=coords,vertex.label =' ')
      dev.off()

      time.taken <- end.time - start.time
      times_louvain<-append(times_louvain,c(file,round(time.taken,4)))
      modularity_louvain.values<-append(modularity_louvain.values,c(file,modularity(wc)))
      print(paste(loc, substr(file,1,nchar(file)-4), '_louvain.clu' , sep=''))
    } else if (grepl('.net', file)){
      real.file<-paste(loc,file, sep='')
      G <- read_graph(real.file, format =  "pajek")
      start.time <- Sys.time()
      wc <- cluster_louvain(G)
      end.time <- Sys.time()
      
      coords = layout_with_kk(G)
      jpeg(paste(image.folder,substr(file,1,nchar(file)-4), '_louvain.jpg' , sep=''))
      plot(wc, G, layout=coords,vertex.label =' ')
      dev.off()
      
      time.taken <- end.time - start.time
      times_louvain<-append(times_louvain,c(file,round(time.taken,4)))
      modularity_louvain.values<-append(modularity_louvain.values,c(file,modularity(wc)))
      print(paste(loc, substr(file,1,nchar(file)-4), '_louvain.clu' , sep=''))
      savePartition(G,wc,paste(loc, substr(file,1,nchar(file)-4), '_louvain.clu' , sep=''))
      
    }
  }
}
B.louvain = matrix( modularity_louvain.values , nrow=length(modularity_louvain.values)/2, ncol=2,byrow=TRUE) 

#####################################################################
#
#Label propagation
#
####################################################################

modularity_label.values<-c()
times_label<-c()

for (folder in problem.type){ 
  loc<-paste(path,folder, sep='')
  files=list.files(loc)
  for (file in files){
    if(grepl('.net', file) & grepl('airports',file)){
      real.file<-paste(loc,file, sep='')
      G <- read_graph(real.file, format =  "pajek")
      start.time <- Sys.time()
      wc <- cluster_label_prop(G)
      end.time <- Sys.time()

      coords = layout_with_fr(G)
      jpeg(paste(image.folder,substr(file,1,nchar(file)-4), '_label_prop.jpg' , sep=''))
      plot(wc, G, layout=coords,vertex.label =' ')
      dev.off()

      time.taken <- end.time - start.time
      times_label<-append(times_label,c(file,round(time.taken,4)))
      modularity_label.values<-append(modularity_label.values,c(file,modularity(wc)))
      print(paste(loc, substr(file,1,nchar(file)-4), '_label_prop.clu' , sep=''))
      savePartition(G,wc,paste(loc, substr(file,1,nchar(file)-4), '_label_prop.clu' , sep=''))
    
    
    } else if (grepl('.net', file)){
      real.file<-paste(loc,file, sep='')
      G <- read_graph(real.file, format =  "pajek")
      start.time <- Sys.time()
      wc <- cluster_label_prop(G)
      end.time <- Sys.time()
      
      coords = layout_with_fr(G)
      jpeg(paste(image.folder,substr(file,1,nchar(file)-4), '_label_prop.jpg' , sep=''))
      plot(wc, G, layout=coords,vertex.label =' ')
      dev.off()
      
      time.taken <- end.time - start.time
      times_label<-append(times_label,c(file,round(time.taken,4)))
      modularity_label.values<-append(modularity_label.values,c(file,modularity(wc)))
      print(paste(loc, substr(file,1,nchar(file)-4), '_label_prop.clu' , sep=''))
      savePartition(G,wc,paste(loc, substr(file,1,nchar(file)-4), '_label_prop.clu' , sep=''))
      
    }
  }
}
B.lp = matrix( modularity_label.values , nrow=length(modularity_label.values)/2, ncol=2, byrow=TRUE) 

#####################################################################
#
# Edge Betweeness
#
####################################################################

modularity_betweenness.values<-c()
times_betweeenness<-c()

for (folder in problem.type){ 
  loc<-paste(path,folder, sep='')
  files=list.files(loc)
  for (file in files){
    if (grepl('.net', file) & grepl('airports',file)){
      real.file<-paste(loc,file, sep='')
      G <- read_graph(real.file, format =  "pajek")
      print(paste('starting with: ', file))
      start.time <- Sys.time()
      wc <- cluster_edge_betweenness(G)
      end.time <- Sys.time()

      time.taken <- end.time - start.time
      print(time.taken)
      coords = layout_with_fr(G)
      jpeg(paste(image.folder,substr(file,1,nchar(file)-4), '_betweenness.jpg' , sep=''))
      plot(wc, G, layout=coords,vertex.label =' ')
      dev.off()
      times_betweeenness<-append(times_betweeenness,c(file,round(time.taken,4)))
      modularity_betweenness.values<-append(modularity_betweenness.values,c(file,modularity(wc)))
      print('Saving it in a file.')
      savePartition(G,wc,paste(loc, substr(file,1,nchar(file)-4), '_betweenness.clu' , sep=''))
      print(paste(file,' done.'))
      
    } else if (grepl('.net', file)){
      real.file<-paste(loc,file, sep='')
      G <- read_graph(real.file, format =  "pajek")
      print(paste('starting with: ', file))
      start.time <- Sys.time()
      wc <- cluster_edge_betweenness(G)
      end.time <- Sys.time()
      
      time.taken <- end.time - start.time
      print(time.taken)
      coords = layout_with_fr(G)
      jpeg(paste(image.folder,substr(file,1,nchar(file)-4), '_betweenness.jpg' , sep=''))
      plot(wc, G, layout=coords,vertex.label =' ')
      dev.off()
      times_betweeenness<-append(times_betweeenness,c(file,round(time.taken,4)))
      modularity_betweenness.values<-append(modularity_betweenness.values,c(file,modularity(wc)))
      print('Saving it in a file.')
      savePartition(G,wc,paste(loc, substr(file,1,nchar(file)-4), '_betweenness.clu' , sep=''))
      print(paste(file,' done.'))
    }
  }
}
B.betweenness = matrix( modularity_betweenness.values , nrow=length(modularity_betweenness.values)/2, ncol=2, byrow=TRUE) 


####################################################################################
####################################################################################
####################################################################################

T.walktrap = matrix( times_walktrap , nrow=length(times_walktrap)/2, ncol=2, byrow=TRUE) 
T.louvain = matrix( times_louvain , nrow=length(times_louvain)/2, ncol=2, byrow=TRUE) 
T.label = matrix( times_label , nrow=length(times_label)/2, ncol=2, byrow=TRUE) 
T.betweenness = matrix( times_betweeenness , nrow=length(times_betweeenness)/2, ncol=2, byrow=TRUE) 
timed=data.frame(T.walktrap[,1],T.louvain[,2],T.label[,2],T.walktrap[,2],T.betweenness[,2])
colnames(timed) <- c("Network Name", "Louvain Method","Label Propagation", "Random Walk", "Edge Betweenness")

save(timed,file="Times.Rda")

#################################################################################
# create a data frame strucutre for the modularity of the partitions and save it#
#################################################################################


modt=data.frame(B.lp[,1],B.louvain[,2],B.lp[,2],B.walktrap[,2],B.betweenness[,2])
colnames(modt) <- c("Network Name", "Louvain Method","Label Propagation", "Random Walk", "Edge Betweenness")

save(modt,file="Modularity.Rda")

# try for one
B.lp



load("Modularity.Rda")
load("Times.Rda")
round_df <- function(x, digits) {
  # round all numeric variables
  # x: data frame 
  # digits: number of digits to round
  #not working for this
  numeric_columns <- sapply(x, mode) == 'numeric'
  x[numeric_columns] <-  round(x[numeric_columns], digits)
  x
}
library(xtable)
xtable(modt)
xtable(timed)

