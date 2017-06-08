
"""
Name: Latex Table Generator based on Partition Comparisson
Author: Pablo Eliseo Reynoso Aguirre
Date: May 7, 2017
Desrcription: Generates a latex table based on radatools partition comparisson files.

"""

measures = ["Network name", 'Jaccard Index', 'Normalized Arithmetic Mutual Information', 'Normalized Variation of Information'];

networks_paths = [

    "All_partition_comp/20x2+5x2_",
    "All_partition_comp/graph3+1+3_",
    "All_partition_comp/graph4+4_",
    "All_partition_comp/star_",
    "All_partition_comp/256_4_4_2_15_18_p_",
    "All_partition_comp/256_4_4_4_13_18_p_",
    "All_partition_comp/rb125_1_",
    "All_partition_comp/rb125_2_",
    "All_partition_comp/rb125_3_",
    "All_partition_comp/cat_cortex_sim_",
    "All_partition_comp/dolphins_",
    "All_partition_comp/football_",
    "All_partition_comp/zachary_unwh_"

];

partition_algorithms = [

    "lp_ctsv",
    "louvain_cstv",
    "rw_ctsv",
    "betw_cstv"
];

file_ext = ".txt";

latex_tables = [];


latex_table_header = "\n\obegin{table}[h]\n\centering\n\obegin{tabular}{|l|l|l|l|l|} \hline"
latex_table_headerf = "\n{$ Real $}   & {$ Obtained $}  & {$ Jaccard Index $} & {$ NAMI $} & {$ NVI $}  \o\ \hline ";
latex_table_footer = " \hline \n\end{tabular}\n\caption{Partitions comparissons in network ABCD}\n\label{tab:networks_models}\n\end{table}";



for path in networks_paths:
    latex_lines = "";
    i = 1;
    for algorithm in partition_algorithms:
        with open(path+algorithm+file_ext, "r") as f:
            lines = f.readlines()
            latex_line = "\n{$ "+lines[0].split("/")[2].strip()+" $} & "+"{$ "+lines[1].split("/")[3].strip()+"$} & {$ "+lines[13].split(":")[1].strip()+"$} & {$ "+lines[19].split(":")[1].strip()+"$} & {$ "+lines[29].split(":")[1].strip()+"$} \o\ ";
            latex_lines += latex_line;
            #print(latex_line);
        i+=1;
    latex_tables.append(latex_table_header+latex_table_headerf+latex_lines+latex_table_footer);


print(latex_tables[1]);

latex_file = open("tables/latex_table_partition_comparissons.txt", "w");
for table in latex_tables:
    latex_file.write(table);
latex_file.close()


