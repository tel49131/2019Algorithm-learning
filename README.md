# 2019Algorithm-learning


# 基本資料
姓名：田安芸
學號：04123036
系級：德文延

# 修課小語 
hi! 我是安芸~ 一名德文系雙主修巨資學院的學生，這學期的演算法讓我備感壓力，因為跟以往上課方式不同，
而且與以前的寫程式的難度提升到一個很難的境界，每次老師給我們的練習題目與作業，說實在我覺得很難。
雖然我的起步跟理解力較慢，期許自己咬著牙撐下去。
我相信經過這次課程我會了解到自己的讀書習慣與方法要如何改變。
即使自己在寫程式上並不熱衷，但還是希望自能夠督促自己把該學的學好。


# 內容
- [week 2](#week-2)
- [week 3](#week-3)
- [week 4](#week-4)
- [week 5](#week-5)
- [week 6](#week-6)
- [week 7](#week-7)

# week 2
 > Topic: Design a linked list
1. What's class?
    * class類別，就是像一個模組，可以產出具有相似特性的實體(物件),也有人會說他像是一個蛋糕模子，可以一直套用 生產蛋糕
    * 底下舉動物的例子，他們都會有相同的"屬性"、不同的"參數"
      譬如，他們都會有"名字"、"物種"的屬性
      每隻動物對應到這個屬性都會有一個特殊的值("參數")
      第一隻動物是名叫"Nico"(名字)的"狗"(物種)
      第二隻動物是名叫"Nana"(名字)的"貓"(物種)
      所以我有一個可以套用的類別，就可以產生無限多隻動物，他們則都有自己的屬性參數

2. What's a linked-list?
   * Linked list(連結串列)是一種常見的資料結構，其使用node(節點)來記錄、表示、儲存資料(data)，並利用每個node中的pointer指向下一個node，藉此將多      個node串連起來，形成Linked list，並以NULL來代表Linked list的終點
     若實際打開每個node的內部，至少會包含(1)data來代表資料，與(2)pointer指向下一個node
 
3. Compare Array and Linked-List
   * 回到今天的主題，在 Python 裏，同樣是陣列，但有 array 和 list 兩種數據類型。兩者的差異在於，前者屬於 Python 模組 numpy 裡的一種數據類型，所包含的所有元素類型都必須相同；而後者則是 Python 內建的數據類型，可以包含不同的元素類型。
   
## reference
1. [CLASS和INSTANCE介紹] https://blog.csdn.net/Hansry/article/details/79639676
2. [python desigh linked-list leetcode] https://blog.csdn.net/fuxuemingzhu/article/details/81026066
3. [array and linked-list] https://ithelp.ithome.com.tw/articles/10203422

# week 3
 > Topic: Stack and Queue
1. What's Stack?
    * Stack(堆疊)是後進來的元素先出去(Last In First Out，縮寫為LIFO)的資料結構，隱含在函式的遞迴呼叫，因為遞迴的過程中最後呼叫的函式要優先處理，系統會實作堆疊程式自動處理遞迴呼叫，不須自行撰寫堆疊，特定問題可能需要使用Stack(堆疊)進行解題，例如：程式的括弧配對檢查，右大括號配對最接近未使用的左大括號，將左大括號加進Stack(堆疊)中，一遇到右大括號就取出配對。

2. What's Queue?
   * Queue(佇列)是先進來的元素先出去(First In First Out，縮寫為FIFO)的資料結構，通常用於讓程式具有排隊功能，依序執行工作，例如：印表機同時間有多個檔案等待列印，在印表機內會有一個Queue(佇列)的功能，將準備列印的檔案暫存在Queue等待印表機提供列印服務，先送到印表機的檔案先印出來。
   
## reference
1. [Stack和Queue介紹] https://sites.google.com/site/zsgititit/home/jin-jiec-cheng-shi-she-ji-2/xian-xing-zi-liao-jie-gou-queue-stack-huolinked-list-yu-you-xian-quan-zhu-lie-priority-queue
2. [python實現stack and queue] https://www.itread01.com/content/1541929816.html
3. [以python實作資料結構] https://super9.space/archives/1105

# week 4
 > Topic: Insertion Sort
1. What's Insertion Sort?
    * 插入排序法(Insertion Sort)是排序演算法的一種，他是一種簡單容易理解的排序演算法，其概念是利用另一個數列來存放已排序部分，逐一取出未排序數列中元素，從已排序數列由後往前找到適當的位置插入。運算流程如下：
    * 從未排序數列取出一元素。
    * 由後往前和已排序數列元素比較，直到遇到不大於自己的元素並插入此元素之後；若都沒有則插入在最前面。
    * 重複以上動作直到未排序數列全部處理完成。

   
## reference
1. [插入排序法(Insertion Sort)] https://emn178.pixnet.net/blog/post/93791164
2. [排序法算法之Insertion Sort] https://blog.csdn.net/xlinsist/article/details/49642565
3. [插入排序法] https://rust-algo.club/sorting/insertion_sort/

# week 5
 > Topic: Quick sort
1. What's Quick Sort?
    * Quick Sort是一種「把大問題分成小問題處理」的分割與征服(Divide and Conquer)方法。
    * 在數列中任意挑選一個數，稱為pivot(可以把它視為基準點)，然後調整數列，使得「所有在pivot左邊的數，都比pivot還小」，而「在pivot右邊的數都比         pivot大」。
    * 接著，將所有在pivot左邊的數視為「新的數列」，所有在pivot右邊的數視為「另一個新的數列」，「分別」重複上述步驟(選pivot、調整數列)，直到分不出      「新的數列」為止。
    * 此外，quick sort 切割後，pivot 並不會傳遞下去，因此每次遞回的總元素數量都會減一。所以在切割的停止時機其實可以設定為，已沒有元素可進行切割時。
    
2.  What's O(n)時間複雜度與空間複雜度?

     (時間複雜度)
     * 由於要將所有元素都與 pivot 比較一遍，因此需要遍歷數列中的所有元素，時間複雜度為 O(n)。
     * 由於切割的大小會隨著 pivot 的不同，而產生不同的子數列，也使得切割次數不定。最佳的情況就是每次都剛好切割為相同大小的子數列，這時候就會使得切        割次數為 log2n 次。
     * 假設每次切割都僅僅將原數列分為 0 與 n - 1（扣除 pivot），也就是說剛好 pivot 都取到該數列中的最大或最小值，則可能會有 n 次的遞回呼叫。所以        quick sort 的時間複雜度分為最佳時為 O(nlog2n)，最差為 O(n2)。
     * 再亂序的情況下，其實要出現剛好跑出 O(n2) 的可能性不高，但因為還是有這可能，所以我們都稱 quick sort 的平攤時間複雜度為 O(nlog2n)，這是對於        quick sort 的排序時間所估算的期望值。
     -----------------------------------------------
     (空間複雜度)
     * 由於每次都會將數列分為兩個子數列，因此會申請兩個新的子數列記憶體空間，對於每個遞回來說空間複雜度是 O(n)，根據前面的敘述可以知道遞回呼叫的次        數最佳為 log2n 次，而最差為 n 次！
     * 因此空間複雜度也是最佳 O(nlog2n)，最差為 O(n2)
   
## reference
1. [快速排序法(Quick Sort)] http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html
2. [[演算法] 快速排序法(Quick Sort)] http://notepad.yehyeh.net/Content/Algorithm/Sort/Quick/Quick.php
3. [淺談quick sort] https://blog.kuoe0.tw/posts/2013/03/15/sort-about-quick-sort/
4. [it幫忙 quick sort] https://ithelp.ithome.com.tw/articles/10202330?sc=iThelpR


# week 6
 > Topic: Heap Sort
 1. What's Heap Sort?
    

# week 7
 > Topic: 
