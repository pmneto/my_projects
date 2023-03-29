libraries_needed <- c("AzureGraph","tidyverse","Microsoft365R")


for(i in libraries_needed){
  
  if (!require(i)) install.packages(i)
  library(i, character.only = TRUE)
}


# authenticate with AAD
# - on first login, call create_graph_login()
# - on subsequent logins, call get_graph_login()
check_credentials <- get_graph_login()

if (length(check_credentials) == 0) create_graph_login()

sharepoint_list <- list_sharepoint_sites()

#Desenvolvimento interrompido, não há justificativa para desenvolver esse projeto