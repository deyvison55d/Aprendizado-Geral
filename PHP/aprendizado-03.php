<!-- Aplica 10% de juros em um produto -->
 <!DOCTYPE html>
 <html lang="pt-br">
 <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
 </head>
 <body>
    <div>
        <?php
            $preco = $_GET['p'];
            echo "O preço do produto é R$ $preco";
            $preco += ($preco*0.1);
            echo "<br>E o novo preço com 10% de aumento será R$ $preco";
            #slk cachoeiraaaaaaaa
        ?>
    </div>
 </body>
 </html>