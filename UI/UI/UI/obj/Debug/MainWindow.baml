   M S B A M L   `   `   `  ����=  9UI, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullclr-namespace:UIUI  5   	       UI.MainWindow   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   "localclr-namespace:UI     5   	     � Title$  
MainWindow��5   	   $	��350��6   $	��525��6)   .��5	      � .+�5
   
   � $
��Left=�6   $	��108��6*   $��	10,10,0,0q�67   $	��Top=�6J   $	��205��6b   .+�5      �� $��帳密設定��6   $
��Left=�6#   $��	10,10,0,0q�6>   $	��Top=�6Q   �� 5      -   5         ��Name$ Account_box��5      $��23��6+   $��
51,41,10,0q�67    �� TextWrapping$
 Wrap=�6K   $��johnplugintw@gmail.com��6_   $	��Top=�6}   �� 5      $��帳號��6   $
��Left=�6!   $��6,41,0,0q�6<   $	��Top=�6N   �� 5      $��密碼��6   $
��Left=�6!   $��6,72,0,0q�6<   $	��Top=�6N   �� 5      -   5        $ Password_box��5      $��23��6,   $��
51,72,10,0q�68   $
 Wrap=�6L   $��Aa123456��6`   $	��Top=�6p   5      � 5   
   $
��Left=�6   $	��294��6*   $��
220,16,0,0q�67   $	��Top=�6K   $	��287��6c   .+�5      �� $��好友列表��6   $
��Left=�6#   $��10,4,0,0q�6>   $	��Top=�6P   &   System.Windows.Controls.DataGrid  5      -   5          Name$ Friend_List_Grid��5      $
��Left=�61   $	��249��6L   $��	10,35,0,0q�6Y   $	��Top=�6l   $	��267��6�      Columns 5      4  .System.Windows.Controls.DataGridTemplateColumn  5      ,  &System.Windows.Controls.DataGridColumn   Header$ 用戶名稱��6-      CellTemplate 5      �� 5      .R�5   "   �� ��6-   �� *Name+5      5        5      $	 mid��6-    5      �� 5       .R�5!   "   �� ��6-   �� *mid+5"      5$      5&      5'      � 5(   
   $
��Left=�6   $	��187��6*   $��
10,123,0,0q�67   $	��Top=�6K   $	��205��6c   .+�5)      �� -   5        $��啟動��5)      $
��Left=�6"   $��	10,10,0,0q�6=   $	��Top=�6P   $��75��6h   6s   �� 5*      -   5         ��Name$ Renew_Friend_List_Btn��5*      $��更新好友列表��64   {�.  $
��Left=�6W   $��
108,10,0,0q�6r   $	��Top=�6�   $��87��6�   6�   5+      5,      5-      