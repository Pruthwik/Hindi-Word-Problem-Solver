How to run the code
python use_saved_model_to_predict_equations.py hindi_question model_path
Sample Execution:
python use_saved_model_to_predict_equations.py "सोहन ने 7.423 की.ग्रा. चावल तथा 6.129 की.ग्रा. दाल खरीदी। सोहन ने कुल कितना सामान खरीदा?" hindi_model.pt
Sample Output:
Question is: सोहन ने 7.423 की.ग्रा. चावल तथा 6.129 की.ग्रा. दाल खरीदी। सोहन ने कुल कितना सामान खरीदा?
Equation is: x = + 7.423 6.129
Solution is: x = 13.552

How to cite this work:
This code is developed as a part of the paper accepted in the LREC-2022 conference. The paper can be cited as:
@InProceedings{sharma-mishra-sharma:2022:LREC,
  author    = {Sharma, Harshita  and  Mishra, Pruthwik  and  Sharma, Dipti},
  title     = {HAWP: a Dataset for Hindi Arithmetic Word Problem Solving},
  booktitle      = {Proceedings of the Language Resources and Evaluation Conference},
  month          = {June},
  year           = {2022},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {3479--3490},
  abstract  = {Word Problem Solving remains a challenging and interesting task in NLP. A lot of research has been carried out to solve different genres of word problems with various complexity levels in recent years. However, most of the publicly available datasets and work has been carried out for English. Recently there has been a surge in this area of word problem solving in Chinese with the creation of large benchmark datastes. Apart from these two languages, labeled benchmark datasets for low resource languages are very scarce. This is the first attempt to address this issue for any Indian Language, especially Hindi. In this paper, we present HAWP (Hindi Arithmetic Word Problems), a dataset consisting of 2336 arithmetic word problems in Hindi. We also developed baseline systems for solving these word problems. We also propose a new evaluation technique for word problem solvers taking equation equivalence into account.},
  url       = {https://aclanthology.org/2022.lrec-1.373}
}
The Hindi Arithmetic Word Problem dataset can be downloaded from https://github.com/hellomasaya/hawp
