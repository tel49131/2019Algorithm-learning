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
    * 堆積排序(Heap Sort)演算法是利用完全二元樹(Complete Binary Tree)，也就是堆積(Heap)結構來完成排序的演算法。
    * 堆積排序有法兩個大步驟，第一個是把要排序的陣列製作成「最小堆積」(Min Heap)或是「最大堆積」(Max Heap)。
    
 2. What's Heap Three?
    * 二元樹的一種 ⇒ 每個父節點最多兩個子節點。
    * 堆積樹為完全二元樹(Complete Binary Tree)的一種。
    * 根據上面的介紹，Heap Sort 可以用兩種方法，第一種是「最小堆積(Min Heap)：父節點的值小於子節點」、第二種是「最大堆積(Max Heap)：父節點的值大於       子節點」。在 min heap裡root一定是所有節點最小的，而在 max heap裡root一定是所有節點最大的。
    (放圖)
    * 還有一個很重要的一點就是，所有的節點都必須由左至右開始。
    
 ## reference
1. [堆積排序法(Heap Sort)] https://magiclen.org/heap-sort/
2. [[演算法] 堆積排序法(Heap Sort)] http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php資料結構 - 二元樹(Binary Tree)
3. [資料結構 - 二元樹(Binary Tree)] https://emn178.pixnet.net/blog/post/94164966


# week 7
 > Topic: 
 
# week 8
 > Topic: Binary tree
 
 
 ## reference



# week 9
 > Topic: Binary search tree
 「二元搜尋樹」。放大量數字並且進行排序的資料結構。原理是 Divide and Conquer ，Root居中，左子樹較小或相等，右子樹較大，然後遞迴分割下去。
 「Divide and Conquer」。將大問題不斷切割成兩個或多個小問題，這樣的過程稱作「Divide」，當切割到最後的小問題，若簡單到可以直接解決，就直接使用程式解決，根據問題的需求決定是否要將小問題的解合併或組合成大問題的解，這樣的過程稱作「Conquer」，這是一種演算法解題策略，屬於由上而下(top-down)的解題策略。
 
 ## reference
1. https://sites.google.com/site/zsgititit/home/jin-jiec-cheng-shi-she-ji/fen-er-zhi-zhi-divide-and-conquer-yu-er-yuan-sou-xun-binary-search
2.http://www.csie.ntnu.edu.tw/~u91029/Order.html


# week 10
 > Topic: Red Black tree
 
 
 ## reference


# week 11
 > Topic: Hash table & Hash function
 Hash Table 是儲存 key,value這種mapping關係的一種資料結構。就是用Hash函數運算出來的值，根據key來儲存在數據結構中。存放這些值的數組就稱為Hash Table。Hash Table主要是希望能夠將存放資料的Table大小調到「真正會存放進去Table的資料數量」，也就是「有用到的key數量」。
 
總而言之，Hash Table就是將key(像老師給的範例是用字串)，我們通過Hash Function然後把他們存到這個類似抽屜的資料結構，這就是Hash Table。
但是，
Hash Table很有可能發生Collision，簡單來說Collision就是兩筆資料會存進同一個Table之slot的情形，這樣會讓查詢資料失敗。舉例來說，我們要item1的key但是卻回傳item2的key。

Hash Function是將不定長度訊息的輸入，用演算法將他演算程固定長度的Hash值的輸出，而且所算出來的Hash值必須符合兩個主要條件：
1.	由Hash Value是無法反推出原來的訊息
2.	Hash Value必須隨明文改變而改變
這樣有點深奧難懂，舉例來說，Hash Function就像是一台果汁機，我們把火龍果還有蘋果(data)，利用果汁機(Hash Function)打一打，出來的是火龍果蘋果汁。這個火龍果蘋果汁是獨一無二，而且沒有辦法變回原來的火龍果和蘋果。
之後如果我們把火龍果換成香蕉，打出來的汁也會改變，也就是說經過Hash Function後的值也會跟著改變。
Hash Function其實有很多演算法，我舉例一種老師說的演算法：
1.	Division Method

(Division Method)
就是把大範圍的資料對應到小範圍的裡面，最簡單的方式就是利用取餘數的方式。假設mod是8，那麼
	H(16) = 15 mod 8 = 7 放在第7個抽屜
	H(25) = 25 mod 8 = 1 放在第1個抽屜
以此類推。而此方法最大的優點就是速度非常的快，只要做一次餘數運算就可以。
這個mod可以自己去斟酌，自己去衡量怎麼樣設會比較好。

 
 ## reference
1.https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/
2.http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
3.https://ithelp.ithome.com.tw/articles/10208884

# week 12
 > Topic: Breadth-First Search
 
 BFS原理
Breadth-First-Search 廣度優先搜尋演算法，又可以稱為寬度優先搜尋法或是橫向修先搜尋，是一種圖形搜尋演算法。講Breadth-First-Search之前要先了解甚麼是圖形搜尋演算法，這樣對BFS的原理才好理解。
圖形搜尋演算法(Graph Traversal)，雖然中文翻作圖，但不是我們平常所想像的那種圖，而是由數個點和數個邊所構成的一張圖，點與點之間是由邊連接，表示點之間是有關係的。

BFS類似於二交叉樹的層序遍歷演算法，其實他的基本原理很簡單，是依靠沿著樹(圖)的寬度遍歷樹的節點，首先我們挑一個起始節點v，然後從v開始，依序訪問v的鄰近還未被訪問的點w1,w2,w3…wn，然後在從w1,w2,w3…wn開始訪問鄰近還未被訪問的點。然後再從這些訪問過的點去接著訪問那些訪問過的點的鄰近點，就這樣一直下去，直到每個點都被訪問完。BFS就是把同一深度(level)的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點。(參照我上面的流程圖)。BFS屬於盲目搜索(uninformed search)是利用佇列(Queue)來處理，通常以迴圈的方式呈現。
 
 
 ## reference
1.http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html
2.https://www.itread01.com/content/1541841612.html
3.https://jason-chen-1992.weebly.com/home/-graph-searching-methods

# week 13
 > Topic: Depth-First Search
 Depth-First-Search深度優先搜尋演算法，是一種遍歷樹或圖形搜尋的演算法。DFS的原理其實也很簡單，是依靠沿著樹(圖)的深度遍歷樹的節點，儘可能深的搜尋樹的分支。當起始節點v的所在邊都己被探尋過，要回溯到發現節點v的那條邊的起始節點。這個過程會一直進行到已發現從源節點可達的所有節點為止。如果還存在未被發現的節點，則選擇其中一個作為源節點並重複以上過程，整個行程反覆進行直到所有節點都被訪問完為止。屬於盲目搜尋。
 
 
 ## reference
1.https://www.itread01.com/content/1546369025.html


# week 14
 > Topic: Minimum Spanning Tree
最為代表是Kruskal
Kruskal是採用邊貪心策略。最基本的就是在初始狀態時隱去圖中的所有邊，每個點都是一個個體，然後接下來就按步驟
1.	對所有的邊按邊權從小到大進行排序
2.	然後按邊權從小到大試所有的邊，如果現在測的邊所連線的兩個頂點不再同一個連通塊中，則可以取用這條邊
3.	執行第二個步驟，直到取到邊的個數是點的個數少1
4.	注意不能形成circle

 
 ## reference
1.https://ithelp.ithome.com.tw/articles/10209593
2.https://www.youtube.com/watch?v=NLp9C7AvJhk
3.http://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html
4.https://wiki.mbalib.com/zh-tw/Dijkstra%E7%AE%97%E6%B3%95
5.https://www.youtube.com/watch?v=wuU4DDEUu1w
6.https://sites.google.com/site/zsgititit/home/jin-jiec-cheng-shi-she-ji-2/zui-xiao-sheng-cheng-shu

# week 15
 > Topic: Shortest Path
最為代表是Dijkstra
Dijkstra Algorithm 是最短路徑演算法的其中一種方法，其主要運作是指定一個始點到其餘各個頂點的最短路徑，也稱之為「單源最短路徑」。從始點開始，每一次一定要堅守一個原則就是由最短距離的開始，所以每次新擴展一個距離最短的時，同時也要更新與其相鄰的幾個點的距離。還有另一個重點是，所有的邊都不可能有負值，因為所以距離都會是正的。然後在更新時一定要細心，因為其實最短路徑的問題會跟邊數成正比，若有一條邊沒有看到那麼可能最不會找到最短路徑。


 ## reference
1.https://ithelp.ithome.com.tw/articles/10209593
2.https://www.youtube.com/watch?v=NLp9C7AvJhk
3.http://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html
4.https://wiki.mbalib.com/zh-tw/Dijkstra%E7%AE%97%E6%B3%95
5.https://www.youtube.com/watch?v=wuU4DDEUu1w
6.https://sites.google.com/site/zsgititit/home/jin-jiec-cheng-shi-she-ji-2/zui-xiao-sheng-cheng-shu

# week 16
 > Topic: 區塊鏈demo & overview

# week 17
 > Topic: 期末考

# week 1
 > Topic: 學期結束
