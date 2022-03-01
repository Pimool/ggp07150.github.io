install.packages("dplyr")
install.packages("Dict")
library(dplyr)
library(Dict)

split_func = function(df){
  
  print("처음 5행입니다.")
  print(df[1:5,])
  
  print("column들입니다")
  print(colnames(df))
  
  conditions = c()
  targets = c()
  
  
  while (TRUE){
    
    input = readline("분리할 column을 순서대로 입력해주세요(더 없다면 Enter) : ")
    
    if (input == ""){
      print("분리할 column들은 다음과 같습니다.")
      print(conditions)
      break
    }
    
    # %in% method : checks whether a vector contains the given element    
    else if (!(input %in% colnames(df))){
      message(sprintf("%s라는 column은 없습니다", input))
    }
    
    else if (input %in% conditions){
      message(sprintf("%s는 이미 선택하셨습니다", input))
    }
    
    else {
      conditions = c(conditions, input)
      print(conditions)
    }
  }
  
  while (TRUE){
    
    input = readline("표시할 column을 순서대로 입력해주세요(더 없다면 Enter) : ")
    
    if (input == ""){
      print("표시할 column들은 다음과 같습니다.")
      print(targets)
      break
    }
    
    else if (!(input %in% colnames(df))){
      message(sprintf("%s라는 column은 없습니다", input))
    }
    
    else if (input %in% conditions){
      message(sprintf("%s는 분리할 column입니다", input))
    }
    
    else if (input %in% targets){
      message(sprintf("%s는 이미 선택하셨습니다", input))
    }
    
    else {
      targets = c(targets, input)
      print(targets)
    }
  }
  
  
  df_target = subset(df, select = targets)
  print(df_target[1:5,])
  
  df_dic = Dict$new(None = NULL)
  cnt = 0
  name_list = c()
  
  #nrow() : 행 개수, length() : 열 개수
  for (row_num in 1:nrow(df)){
    df_condition = df[row_num, conditions]   # row_num번째 condition들만 열로 있는 row
    value_vector = as.vector(t(df_condition))   # 한 행 짜리 df를 vector로 바꿈
    one_line = paste(value_vector, collapse = "_")
    name = paste0("patient_count", one_line)
    
    if (df_dic$has(name)){
      df_dic[name] = rbind(df_dic[name], df_target[row_num, , drop = FALSE])
    }
    
    else{
      df_dic[name] = df_target[row_num, , drop = FALSE]
      cnt = cnt+1
      name_list = c(name_list, name)
    }
  }
  df_dic$remove("None")
  
  for (index in 1:cnt){
    assign(name_list[index], df_dic[index], envir = .GlobalEnv)
  }
  
} 