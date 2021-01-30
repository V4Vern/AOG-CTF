<!DOCTYPE html>
<html lang="en">

    <head>

        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="">
        <meta name="author" content="">

        <title>Blog Post </title>

        <!-- Bootstrap core CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

        <!-- Custom styles for this template -->
        <link href="blog-post.css" rel="stylesheet">

    </head>

    <body>

        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
            <div class="container">
                <a class="navbar-brand" href="index.php">Blog</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </nav>

        <!-- Page Content -->
        <div class="container">
            <div class="row">
                <!-- Post Content Column -->
                <div class="col-lg-12">
                    <!-- Title -->
                    <h1 class="mt-4">Business Factory Inc</h1>

                    <!-- Author -->
                    <p class="lead">
                        by
                        <a href="#">Admin</a>
                    </p>

                    <hr>
                    <?php
                    if (!isset($_GET['id']))
                        die("No ID specified.");
                    $pressID = (int) $_GET['id'];
                    switch ($pressID) {
                        case 1:
                            echo <<<'EOD'
		<h2>Business Factory Announces Plans For New Headquarters in Argleton, England</h2>
		<p><b>San Francisco, CA &mdash; 01 January 2020 &mdash;</b> Business Factory is pleased to announced that we have chosen Argleton, England as the location for our new headquarters.</p><p> With its rich history and diverse people, this is a great strategic move for us. Business Factory will invest $10 gazillion and create a lot of jobs (like, a LOT).</p><p> "I'm really excited for this move. It'll go off without any problems I'm sure" said Joe Bloggs, CEO of Business Factory.</p>
EOD;
                            break;
                        case 2:
                            echo <<<'EOD'
		<h2>Statement on Planned Expansion to Argleton</h2>
		<p><b>San Francisco, CA &mdash; 30 January 2020 &mdash;</b>After lots of deliberation, Business Factory has decided to cancel its plans for a new headquarters in Argleton, England.</p><p>This decision has been made after media reports stated that Argleton was not a real place.</p><p>"Apparently one of my friends thought it'd be funny to try and convince me that Argleton was an actual place, and he described it as being so great I thought it would be a good idea to set up something there. I'm gonna have a nice long chat with him later" said Joe Bloggs, CEO of Business Factory.</p><p>At present, Business Factory is evaluating Finland as a possible location for a new HQ, but only after determining whether it actually exists.</p>
EOD;
                            break;
                        case 3:
                            echo <<<'EOD'
		<h2>Statement on Reports of Asbestos Contamination</h2>
		<p><b>San Francisco, CA &mdash; 01 February 2020 &mdash;</b>Business Factory would like to catergorically state that any reports of an asbestos infestation in our California offices are false and we will sue the hell out of anyone who insinuates otherwise.</p><p>"It's not funny guys" said Joe Bloggs, CEO of Business Factory. <!-- Let's be real, it kind of is. - Press Release Writer--></p>
EOD;
                            break;
                        case 4:
                            echo <<<'EOD'
		<h2>Business Factory Teams Up with Uber, Google, Venture Capital Firms to End Workplace Harassment</h2>
		<p><b>San Francisco, CA &mdash; 30 February 2020 &mdash;</b>Business Factory is teaming up with major tech firms Google and Uber as well as a selection of venture capital firms to push for anti-harassment policies across the industry.</p><p>"I don't think these guys have had any major controversies regarding that subject so they're pretty good role models I think" said Joe Bloggs, CEO of Business Factory.</p><p><b>Update (6 October):</b> Business Factory have suspended this initiative as new information has come to light.</p>
EOD;
                            break;
                        case 100:
                            echo <<<'EOD'
		<h2>Business Factory Brings In New CEO</h2>
		<p><b>San Francisco, CA &mdash; 30 November 2022 &mdash;</b>Business Factory is announcing today that it is bringing on John Smith, previously CEO of Very Stealth Startup (before that imploded), to replace our previous CEO Joe Bloggs.</p><p>"There wasn't any serious character flaw in him or whatever, but to be honest the past year has shown that he is a bit of a dumbass. Anyway we are going to put all of that behind us now" said Joe Smith.</p><p>Hey, what are you doing here? Scram. Oh, fine, here's a flag for you: <b>19C4{i+s_Just_arithmetic}</b></p>
EOD;
                            break;
                        default:
                            echo <<<'EOD'
		<h2>Error 404 </h2>
        <p> Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</p>
EOD;
                    }
                    ?>

                    <hr>

                </div>

                <!-- Sidebar Widgets Column -->
                <div class="col-md-12">
                    <!-- Side Widget -->
                    <div class="card my-4">
                        <h5 class="card-header">News </h5>
                        <div class="card-body">
                            This page contains all the interesting news in 2020
                        </div>
                    </div>

                </div>


            </div>
            <!-- /.row -->

        </div>
        <!-- /.container -->

        <!-- Footer -->
        <footer class="page-footer font-small blue">

            <!-- Copyright -->
            <div class="footer-copyright text-center py-3">© 2020 Copyright:
                <a href="https://mdbootstrap.com/"> MDBootstrap.com</a>
            </div>
            <!-- Copyright -->

        </footer>
        <!-- Footer -->
        <!-- Bootstrap core JavaScript -->
        <!-- JS, Popper.js, and jQuery -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>

    </body>
</html>
