# 归并排序C++版本
## 第一版
```
#include<iostream>
//9 6 7 22 20 33 16 20
using namespace std;

//归并已经排序的好的数据 自上而上
void Merge(int data[],int start,int ends,int result[]){
    int left_length = (ends - start + 1)/2 + 1; //左侧集合的长度
    int left_index = start; //左侧集合的起始下标
    int right_index = start + left_length; //右侧集合的起始下标
    int result_index = start; //结果存储的起始下标
    //将左右侧集合归并到一起
    while(left_index < start + left_length && right_index < ends + 1){
        if(data[left_index] <= data[right_index]){
            result[result_index] = data[left_index];
            left_index++;
            result_index++;
        }
        else{
            result[result_index] = data[right_index];
            right_index++;
            result_index++;
        }
    }
    //将左侧或右侧集合剩余的添加进去
    while(left_index < start + left_length){
        result[result_index] = data[left_index];
        left_index++;
        result_index++;
    }
    while(right_index < ends + 1){
        result[result_index] = data[right_index];
        right_index++;
        result_index++;
    }
}

//划分过程 自上而下
void Merge_Sort(int data[],int start,int ends,int result[]){
    //如果有两个元素则进行排序
    if(ends - start == 1){
        if(data[ends] < data[start]){
            int temp = data[start];
            data[start] = data[ends];
            data[ends] = temp;
        }
        return;
    }
    //否则如果有一个元素则不排序
    else if(ends - start == 0){
        return;
    }
    //如果都不是则继续划分 一分为二
    else{
        Merge_Sort(data,start,(ends-start+1)/2+start,result);
        Merge_Sort(data,(ends-start+1)/2+start+1,ends,result);
        Merge(data,start,ends,result);
        for(int i=0;i<=ends;i++){
            data[i] = result[i];
        }
    }
}

int main(){
    int num;
    cin>>num;
    int qwe[num],result[num];
    for(int i=0;i<num;i++){
        cin>>qwe[i];
    }
    Merge_Sort(qwe,0,num-1,result);
    for(int i=0;i<num;i++){
        cout<<qwe[i]<<" ";
    }
    cout<<endl;
    return 0;
}

```

## 第二版
```
#include<iostream>
#include<algorithm>

using namespace std;

//归并排序
bool merge_sort(int *init,int num){
    int step = 2;
    while(step<num){
        int index = 0;
        while(true){
            if(index + step >= num){
                sort(init+index,init+num,less<int>());
                break;
            }
            else{
                sort(init+index,init+index+step,less<int>());
                index += step;
            }
        }
        step = step * 2;
    }
    int index = 0;
    while(true){
        if(index + step >= num){
            sort(init+index,init+num,less<int>());
            break;
        }
        else{
            sort(init+index,init+index+step,less<int>());
            index += step;
        }
    }
    for(int i=0;i<num;i++){
        if(i == num-1){
            cout<<init[i];
        }
        else{
            cout<<init[i]<<" ";
        }
    }
}

int main(){
    int num;
    cin>>num;
    int init[num],target[num],backup[num];
    for(int i=0;i<num;i++){
        cin>>init[i];
        backup[i] = init[i];
    }
    merge_sort(init,num);
    return 0;
}

```