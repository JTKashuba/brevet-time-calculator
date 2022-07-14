<html>
    <head>
        <title>CIS 322 REST-api demo: Laptop list</title>
    </head>

    <body>
        <h1>List of Control Points/Times</h1>
        <ul>
            <h2> List of ALL control points open/close times </h2>
            <?php
            $json = file_get_contents('http://laptop-service/listAll');
            $obj = json_decode($json);
	          $laptops = $obj->Laptops;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            ?>

            <h2> List of all control points OPEN times </h2>
            <?php
            $json = file_get_contents('http://laptop-service/listOpenOnly');
            $obj = json_decode($json);
	          $laptops = $obj->Laptops;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            ?>

            <h2> List of all control points CLOSE times </h2>
            <?php
            $json = file_get_contents('http://laptop-service/listCloseOnly');
            $obj = json_decode($json);
	          $laptops = $obj->Laptops;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>
    </body>
</html>
