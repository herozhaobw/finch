<img src="https://github.com/zhedongzheng/finch/blob/master/assets/transformer.png" width="300">

This project is built upon [Kyubyong's](https://github.com/Kyubyong/transformer) work, thanks for him!

* Based on that, we have:
  * implemented the model under the architecture of ```tf.estimator.Estimator``` API
  
  * added an option to share the weights between encoder embedding and decoder embedding
  
  * added an option to share the weights between decoder embedding and output projection
  
  * added the learning rate variation according to the formula in paper, and also expotential decay
  
  * added more activation choices (leaky relu / elu) for easier gradient propagation
  
  * generated the key and query masks before positional encoding
  
    * because after positional encoding, the paddings in key and query will move from zeros to other values

* Small Task 1: learn sorting characters
    * ``` python train_letters.py --tie_embedding```
    * greedy sampling after 4692 steps
        ```
        apple -> aelpp
        common -> cmmnoo
        zhedong -> deghnoz
        ```
* Small Task 2: learn chinese chatting
    * ``` python train_dialog.py```
    * greedy sampling after 10000 steps
        ```
        你是谁 -> 我是小通
        你喜欢我吗 -> 我喜欢你
        给我唱一首歌 -> =。=
        我帅吗 -> 我是帅哥
        ```
<img src="https://github.com/zhedongzheng/finch/blob/master/assets/transform20fps.gif" height='400'>
