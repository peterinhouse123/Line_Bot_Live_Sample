using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using WebSocketSharp;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using System.Windows.Threading;
using System.Collections.ObjectModel;

namespace UI
{
    /// <summary>
    /// MainWindow.xaml 的互動邏輯
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            //開發用 先行解鎖反灰鈕
            Renew_Friend_List_Btn.IsEnabled = true;
            //目前是開發狀態 ，ws 伺服器已經預先啟動，發行後記得加入ws啟動的流程
            WS_Init();
        }
        private WebSocket WS;

        const string host = "ws://127.0.0.1:6677";

        public void WS_Init()
        {


            WS = new WebSocket(host);

            WS.OnMessage += (ss, ee) => Msg_Decode(ee.Data);
            WS.OnError += (ss, ee) => On_Error_Msg(ee.Message);
          
            WS.Connect();
        }
       
        private void On_Error_Msg (string msg)
        {
            Console.WriteLine(msg);
        }

        private void Msg_Decode(string json)
        {
            Console.WriteLine("ws_接收到訊息：");
            Console.WriteLine(json);

            try
            {
                

                dynamic data = JValue.Parse(json);
                string order = data["order"];
                var detail = data["detail"];

                switch (order)
                {
                    case "login_success":
                        Console.WriteLine("登入成功!~");
                        

                        Dispatcher.Invoke(
                            DispatcherPriority.Normal,
                            new Action <Button, bool>  (Set_Button_Enabled),
                            Renew_Friend_List_Btn, 
                            true                            
                            );


                        break;

                    case "Friend_List":
                        Console.WriteLine("獲取到新的好友清單!~");

                        ObservableCollection<Friend_Item> New_Friend_List = new ObservableCollection<Friend_Item>();

                        foreach (var item in detail)
                        {
                            Console.WriteLine(item["name"]);
                            Friend_Item New_Item = new Friend_Item();
                            New_Item.Name = item["name"];
                            New_Item.mid = item["mid"];
                            New_Friend_List.Add(New_Item);

                        }

                        Dispatcher.Invoke(
                            DispatcherPriority.Normal,
                            new Action<ObservableCollection<Friend_Item>>(Change_Friend_List_Grid),
                            New_Friend_List
                            );


                        break;

                    default:
                        break;
                }



            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                Console.WriteLine(json);
                Console.WriteLine("error_WS_Msg_not a JSON");
            }


        }

        public void Set_Button_Enabled(Button btn, bool bol)
        {
            btn.IsEnabled = bol;
        }

        private void Send_Order(string order, dynamic detail)
        {
            JObject data = new JObject();
            data["order"] = order;
            data["detail"] = detail;

            string json = data.ToString(Formatting.None);

            Console.WriteLine(json);
            WS.Send(json);
        }

        public class Friend_Item
        {

            public string Name { get; set; }
            public string mid { get; set; }

        }

        public void Change_Friend_List_Grid(ObservableCollection<Friend_Item> source)
        {
            Friend_List_Grid.ItemsSource = source;
        }

        private void Start_Login_Btn_fn(object sender, RoutedEventArgs e)
        {
            string Account = Account_box.Text;
            string Password = Password_box.Text;

            JObject acc_pack = new JObject();
            acc_pack["account"] = Account;
            acc_pack["password"] = Password;


            Send_Order("login", acc_pack);
        }

        private void Renew_Friend_List_Btn_Click(object sender, RoutedEventArgs e)
        {
            Send_Order("renew_friend_list", "");

        }
    }
}
