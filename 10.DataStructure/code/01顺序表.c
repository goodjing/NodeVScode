void InitList(SqList &L) //构造一个空的顺序表
{
    L.elem = (ElemType*) malloc (LIST_INIT_SIZE * sizeof(ElemType)); //用指针elem开辟一个大小为LIST_INIT_SIZE  * sizeof(ElemType)的存储空间，LIST_INIT_SIZE 为大小，sizeof(ElemType)为单位
    if (!L.elem)
    {
        exit(OVERFLOW);
    }
    L.length = 0; //空表长度为0
    L.size = LIST_INIT_SIZE ; //空表的初始存储容量
}
