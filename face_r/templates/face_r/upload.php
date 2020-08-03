<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>sample</title>
</head>
<body>
<p><?php
// ファイル名を取得して、ユニークなファイル名に変更
$file_name = $_FILE['upfile']['name'];
$uniq_file_name = date("YmdHis") . "_" . $file_name;
 
// 仮にファイルがアップロードされている場所のパスを取得
$tmp_path = $_FILE['upfile']['tmp_name'];
 
// 保存先のパスを設定
$upload_path = './phototest/';
 
if (is_uploaded_file($tmp_path)) {
  // 仮のアップロード場所から保存先にファイルを移動
  if (move_uploaded_file($tmp_path, $upload_path . $uniq_file_name)) {
    // ファイルが読出可能になるようにアクセス権限を変更
    //chmod($upload_path . $uniq_file_name, 0644);
 
    echo $file_name . "をアップロードしました。";
    echo "<br><a href='photoform.html'><- TOPへ戻る</a>";
  } else {
    echo "Error:アップロードに失敗しました。";
  }
} else {
  echo "Error:画像が見つかりません。";
}
?></p>
</body>
</html>
