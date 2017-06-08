echo -----------------------------------------
echo ----------- Complex Netwokrs ------------
echo --- Practical3 - Community Detection ----
echo --- Heuristic: Maximizing Modularity ----
echo --- Name: Jorge Rodriguez Molinuevo -----
echo ---- Compare Partitions Sub-routine -----
echo -----------------------------------------

echo ----- Toy Networks ----------------------

Compare_Partitions.exe  A3_nets/toy/20x2+5x2.clu A3_nets/toy/comm_detection/20x2+5x2_label_prop.clu A3_nets/toy/partition_comp/20x2+5x2_lp_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/graph3+1+3.clu A3_nets/toy/comm_detection/graph3+1+3_label_prop.clu A3_nets/toy/partition_comp/graph3+1+3_lp_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/graph4+4.clu A3_nets/toy/comm_detection/graph4+4_label_prop.clu A3_nets/toy/partition_comp/graph4+4_lp_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/star.clu A3_nets/toy/comm_detection/star_label_prop.clu A3_nets/toy/partition_comp/star_lp_ctsv.txt  V  4

Compare_Partitions.exe  A3_nets/toy/20x2+5x2.clu A3_nets/toy/comm_detection/20x2+5x2_louvain.clu A3_nets/toy/partition_comp/20x2+5x2_louvain_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/graph3+1+3.clu A3_nets/toy/comm_detection/graph3+1+3_louvain.clu A3_nets/toy/partition_comp/graph3+1+3_louvain_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/graph4+4.clu A3_nets/toy/comm_detection/graph4+4_louvain.clu A3_nets/toy/partition_comp/graph4+4_louvain_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/star.clu A3_nets/toy/comm_detection/star_louvain.clu A3_nets/toy/partition_comp/star_louvain_cstv.txt  V  4

Compare_Partitions.exe  A3_nets/toy/20x2+5x2.clu A3_nets/toy/comm_detection/20x2+5x2_walktrap.clu A3_nets/toy/partition_comp/20x2+5x2_rw_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/graph3+1+3.clu A3_nets/toy/comm_detection/graph3+1+3_walktrap.clu A3_nets/toy/partition_comp/graph3+1+3_rw_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/graph4+4.clu A3_nets/toy/comm_detection/graph4+4_walktrap.clu A3_nets/toy/partition_comp/graph4+4_rw_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/star.clu A3_nets/toy/comm_detection/star_walktrap.clu A3_nets/toy/partition_comp/star_rw_ctsv.txt  V  4

echo ----- Model Networks ----------------------

Compare_Partitions.exe  A3_nets/model/256_4_4_2_15_18_p.clu A3_nets/model/comm_detection/256_4_4_2_15_18_p_label_prop.clu A3_nets/model/partition_comp/256_4_4_2_15_18_p_lp_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/model/256_4_4_4_13_18_p.clu A3_nets/model/comm_detection/256_4_4_4_13_18_p_label_prop.clu A3_nets/model/partition_comp/256_4_4_4_13_18_p_lp_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-1.clu A3_nets/model/comm_detection/rb125_label_prop.clu A3_nets/model/partition_comp/rb125_1_lp_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-2.clu A3_nets/model/comm_detection/rb125_label_prop.clu A3_nets/model/partition_comp/rb125_2_lp_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-3.clu A3_nets/model/comm_detection/rb125_label_prop.clu A3_nets/model/partition_comp/rb125_3_lp_ctsv.txt  V  4

Compare_Partitions.exe  A3_nets/model/256_4_4_2_15_18_p.clu A3_nets/model/comm_detection/256_4_4_2_15_18_p_louvain.clu A3_nets/model/partition_comp/256_4_4_2_15_18_p_louvain_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/model/256_4_4_4_13_18_p.clu A3_nets/model/comm_detection/256_4_4_4_13_18_p_louvain.clu A3_nets/model/partition_comp/256_4_4_4_13_18_p_louvain_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-1.clu A3_nets/model/comm_detection/rb125_louvain.clu A3_nets/model/partition_comp/rb125_1_louvain_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-2.clu A3_nets/model/comm_detection/rb125_louvain.clu A3_nets/model/partition_comp/rb125_2_louvain_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-3.clu A3_nets/model/comm_detection/rb125_louvain.clu A3_nets/model/partition_comp/rb125_3_louvain_cstv.txt  V  4


Compare_Partitions.exe  A3_nets/model/256_4_4_2_15_18_p.clu A3_nets/model/comm_detection/256_4_4_2_15_18_p_walktrap.clu A3_nets/model/partition_comp/256_4_4_2_15_18_p_rw_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/model/256_4_4_4_13_18_p.clu A3_nets/model/comm_detection/256_4_4_4_13_18_p_walktrap.clu A3_nets/model/partition_comp/256_4_4_4_13_18_p_rw_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-1.clu A3_nets/model/comm_detection/rb125_walktrap.clu A3_nets/model/partition_comp/rb125_1_rw_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-2.clu A3_nets/model/comm_detection/rb125_walktrap.clu A3_nets/model/partition_comp/rb125_2_rw_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-3.clu A3_nets/model/comm_detection/rb125_walktrap.clu A3_nets/model/partition_comp/rb125_3_rw_ctsv.txt  V  4


echo ----- Real Networks ----------------------


Compare_Partitions.exe  A3_nets/real/cat_cortex_sim.clu A3_nets/real/comm_detection/cat_cortex_sim_label_prop.clu A3_nets/real/partition_comp/cat_cortex_sim_lp_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/real/dolphins-real.clu A3_nets/real/comm_detection/dolphins_label_prop.clu A3_nets/real/partition_comp/dolphins_lp_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/real/football-conferences.clu A3_nets/real/comm_detection/football_label_prop.clu A3_nets/real/partition_comp/football_lp_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/real/zachary_unwh-real.clu A3_nets/real/comm_detection/zachary_unwh_label_prop.clu A3_nets/real/partition_comp/zachary_unwh_lp_ctsv.txt  V  4

Compare_Partitions.exe  A3_nets/real/cat_cortex_sim.clu A3_nets/real/comm_detection/cat_cortex_sim_louvain.clu A3_nets/real/partition_comp/cat_cortex_sim_louvain_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/real/dolphins-real.clu A3_nets/real/comm_detection/dolphins_louvain.clu A3_nets/real/partition_comp/dolphins_louvain_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/real/football-conferences.clu A3_nets/real/comm_detection/football_louvain.clu A3_nets/real/partition_comp/football_louvain_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/real/zachary_unwh-real.clu A3_nets/real/comm_detection/zachary_unwh_louvain.clu A3_nets/real/partition_comp/zachary_unwh_louvain_cstv.txt  V  4


Compare_Partitions.exe  A3_nets/real/cat_cortex_sim.clu A3_nets/real/comm_detection/cat_cortex_sim_walktrap.clu A3_nets/real/partition_comp/cat_cortex_sim_rw_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/real/dolphins-real.clu A3_nets/real/comm_detection/dolphins_walktrap.clu A3_nets/real/partition_comp/dolphins_rw_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/real/football-conferences.clu A3_nets/real/comm_detection/football_walktrap.clu A3_nets/real/partition_comp/football_rw_ctsv.txt  V  4
Compare_Partitions.exe  A3_nets/real/zachary_unwh-real.clu A3_nets/real/comm_detection/zachary_unwh_walktrap.clu A3_nets/real/partition_comp/zachary_unwh_rw_ctsv.txt  V  4


echo ----- Leading Eigenvector for all Networks ----------------------


Compare_Partitions.exe  A3_nets/real/cat_cortex_sim.clu A3_nets/real/comm_detection/cat_cortex_sim_betweenness.clu A3_nets/real/partition_comp/cat_cortex_sim_betw_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/real/dolphins-real.clu A3_nets/real/comm_detection/dolphins_betweenness.clu A3_nets/real/partition_comp/dolphins_betw_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/real/football-conferences.clu A3_nets/real/comm_detection/football_betweenness.clu A3_nets/real/partition_comp/football_betw_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/real/zachary_unwh-real.clu A3_nets/real/comm_detection/zachary_unwh_betweenness.clu A3_nets/real/partition_comp/zachary_unwh_betw_cstv.txt  V  4

Compare_Partitions.exe  A3_nets/model/256_4_4_2_15_18_p.clu A3_nets/model/comm_detection/256_4_4_2_15_18_p_betweenness.clu A3_nets/model/partition_comp/256_4_4_2_15_18_p_betw_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/model/256_4_4_4_13_18_p.clu A3_nets/model/comm_detection/256_4_4_4_13_18_p_betweenness.clu A3_nets/model/partition_comp/256_4_4_4_13_18_p_betw_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-1.clu A3_nets/model/comm_detection/rb125_betweenness.clu A3_nets/model/partition_comp/rb125_1_betw_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-2.clu A3_nets/model/comm_detection/rb125_betweenness.clu A3_nets/model/partition_comp/rb125_2_betw_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/model/rb125-3.clu A3_nets/model/comm_detection/rb125_betweenness.clu A3_nets/model/partition_comp/rb125_3_betw_cstv.txt  V  4

Compare_Partitions.exe  A3_nets/toy/20x2+5x2.clu A3_nets/toy/comm_detection/20x2+5x2_betweenness.clu A3_nets/toy/partition_comp/20x2+5x2_betw_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/graph3+1+3.clu A3_nets/toy/comm_detection/graph3+1+3_betweenness.clu A3_nets/toy/partition_comp/graph3+1+3_betw_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/graph4+4.clu A3_nets/toy/comm_detection/graph4+4_betweenness.clu A3_nets/toy/partition_comp/graph4+4_betw_cstv.txt  V  4
Compare_Partitions.exe  A3_nets/toy/star.clu A3_nets/toy/comm_detection/star_betweenness.clu A3_nets/toy/partition_comp/star_betw_cstv.txt  V  4


