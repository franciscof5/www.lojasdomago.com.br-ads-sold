<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        teste nbody
        <?php
        $path = '.';
        $results = scandir($path);
        
        foreach ($results as $result) {
            if ($result === '.' or $result === '..') continue;

            if (is_dir($path . '/' . $result) && $result!=".git" && $result!="_vend-itape") {
                echo "<h1>$result</h1>";    
                //code to use if directory
                $subdir = scandir($result);
                
                foreach ($subdir as $result2) {
                    if ($result2 === '.' or $result2 === '..') continue;
                    echo "<hr /><h2>$result2</h2";

                    if (is_dir($path . '/' . $result2)) {
                        echo "<h4>$result2</h4>";
                        $subsubdir = scandir($path . '/' . $result2);
                        var_dump($subsubdir);
                        foreach ($subdirdir as $subsubdir2) {
                            echo "XXX:?".$subsubdir2;
                            $img = scandir($path . '/' . $result2 . '/' . $subsubdir2);
                            foreach($subsubdir2 as $img) {
                                if(substr($img,-3)=="jpg")
                                    echo "<img src='".$img."' width='300'><br>";
                                else
                                    echo $img;
                            }
                        }
                    }

                }
                
            }
        }
        ?>
    </body>
</html>