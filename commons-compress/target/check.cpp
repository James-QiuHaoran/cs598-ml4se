

int main(){

  auto s1 = __hpvm_section_begin();
  auto t1 = __hpvm_task_begin();
  
  auto s2 = __hpvm_section_begin();

  auto subt1 = task_begin();


  __hpvm_task_end(subt1);


  auto subt2 = task_begin();

  __hpvm_task_end(subt2);

  // subt3
  
  // subt4

  __hpvm_section_end();


  __hpvm_task_end(t1);


  // t2 dependent on t1
  auto t2 = __hpvm_task_begin();

  // ...

  __hpvm_task_end(t2);
  __hpvm_section_end(s1);

  return 0;
}

void kernel1(ptr1, p1Size, ptr2, p2Size); 
void kernel2(ptr2, p2Size, ptr3, p3Size); 

