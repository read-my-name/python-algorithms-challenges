# 选择排序
def selectsort(s):
    for i in range(0,len(s)-1):
        curmin=inf
        curidx=-1
        for j in range(i,len(s)):
            if s[j]<curmin:
                curmin=s[j]
                curidx=j
        if curidx!=-1:
            s[i],s[curidx]=s[curidx],s[i]

#冒泡排序
def bubblesort(s):
    for i in range(len(s)-1,-1,-1):
        for j in range(0,i):
            if s[j]>s[j+1]:
                s[j+1],s[j]=s[j],s[j+1]

#插入排序
def insertsort(s):
    n=len(s)
    for i in range(1,n):
        x=s[i]
        j=i-1
        while j>=0:
            if x<=s[j]:
                s[j+1]=s[j]
                j-=1
            else:
                break
        s[j+1]=x

#归并排序
def merge(s,start,mid,end):
    tmp=[]
    l=start
    r=mid+1
    while l<=mid and r<=end:
        if s[l]<=s[r]:
            tmp.append(s[l])
            l+=1
        else:
            tmp.append(s[r])
            r+=1
    tmp.extend(s[l:mid+1])
    tmp.extend(s[r:end+1])
    for i in range(start,end+1):
        s[i]=tmp[i-start]
def mergesort(s,start,end):
    if start==end:
        return 
    mid=(start+end)//2
    mergesort(s,start,mid)
    mergesort(s,mid+1,end)
    merge(s,start,mid,end)
    
#桶排序（适用于数据分布均匀的排序）
def bucketsort(s):
    maxv=max(s)
    minv=min(s)
    bucket=[[],[],[]]
    bucketCount=3
    perbucket=(maxv-minv+bucketCount)//bucketCount
    for num in s:
        bucketidx=(num-minv)//perbucket
        bucket[bucketidx].append(num)
    for i in range(bucketCount):
        selectsort(bucket[i])
    idx=0
    for i in range(bucketCount):
        for j in bucket[i]:
            s[idx]=j
            idx+=1

#计数排序(适用于数据范围小的排序，空间换时间)
def countsort(s):
    cnt=max(s)+1
    counter=[0]*cnt
    for x in s:
        counter[x]+=1
    s.clear()
    for i in range(len(counter)):
        s.extend([i]*counter[i])

#基数排序
def radixsort(s):
    base=1
    maxv=max(s)
    while base<=maxv:
        bucket=[]
        for idx in range(10):
            bucket.append([])
        for num in s:
            idx=num//base%10
            bucket[idx].append(num)
        l=0
        for idx in range(10):
            for v in bucket[idx]:
                s[l]=v
                l+=1
        base*=10
        
#快速排序
def quicksortpivot(a,start,end):
    pivot=start
    j=start+1
    for i in range(start+1,end+1):
        if a[i]<=a[pivot]:
            a[i],a[j]=a[j],a[i]
            j+=1
    a[pivot],a[j-1]=a[j-1],a[pivot]
    pivot=j-1
    return pivot
def quicksort(a,start,end):
    if start>=end:
        return
    pivot=quicksortpivot(a,start,end)
    quicksort(a,start,pivot-1)
    quicksort(a,pivot+1,end)

#随机快速排序
def quicksortpivot(a,start,end):
    randidx=random.randint(start,end)
    a[start],a[randidx]=a[randidx],a[start]
    pivot=start
    j=start+1
    for i in range(start+1,end+1):
        if a[i]<=a[pivot]:
            a[i],a[j]=a[j],a[i]
            j+=1
    a[pivot],a[j-1]=a[j-1],a[pivot]
    pivot=j-1
    return pivot
def quicksort(a,start,end):
    if start>=end:
        return
    pivot=quicksortpivot(a,start,end)
    quicksort(a,start,pivot-1)
    quicksort(a,pivot+1,end)
    
#希尔排序
def shellsort(a):
    n=len(a)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            x=a[i]
            j=i
            while j>=gap:
                if x<a[j-gap]:
                    a[j]=a[j-gap]
                else:
                    break
                j-=gap
            a[j]=x
        gap//=2

#堆排序
def maxheapify(heap,start,end):
    son=start*2
    while son<=end:
        if son+1<=end and heap[son+1]>heap[son]:
            son+=1
        if heap[son]>heap[start]:
            heap[start],heap[son]=heap[son],heap[start]
            start,son=son,son*2
        else:
            break
def heapsort(a):
    heap=[None]+a
    root=1
    l=len(heap)
    for i in range(l//2,root-1,-1):
        maxheapify(heap,i,l-1)
    for i in range(l-1,root,-1):
        heap[i],heap[root]=heap[root],heap[i]
        maxheapify(heap,root,i-1)
    return heap[root:]