    ];
    for (var x = 0; x < keepers.length; x++) {
        newLanguage[keepers[x]] = Blockly.Language[keepers[x]];
            }
                // Fold control category into logic category.
                /*for (var name in newLanguage) {
                    if (newLanguage[name].category == 'Math') {
                        newLanguage[name].category = 'Logic';
                            }
                                }*/
                            Blockly.Language = newLanguage;
        
            Blockly.inject(document.body, {path: '/'});
                
                if (window.parent.init) {
                    // Let the top-level application know that Blockly is ready.
                    window.parent.init(Blockly);
                } else {
                    // Attempt to diagnose the problem.
                    var msg = 'Error: Unable to communicate between frames.\n\n';
                    if (window.parent == window) {
                        msg += 'Try loading index.html instead of frame.html';
                    } else if (window.location.protocol == 'file:') {
                        msg += 'This may be due to a security restriction preventing\n' +
                            'access when using the file:// protocol.\n' +
                                'http://code.google.com/p/chromium/issues/detail?id=47416';
                    }
        alert(msg);
        }
            }
            
            function load(xmlText) {
                var xmlDom = Blockly.Xml.textToDom(xmlText)
                Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, xmlDom);
            }
            
            function ready() {
                if (window.parent.blocklyReady) {
                    // Let the top-level application know that the frame is ready.
                    window.parent.blocklyReady();
            }
            }

            function getXml() {
                var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
                return Blockly.Xml.domToText(xml);
    }
    </script>
    </head>
    <body  onload="ready()" >
    </body>
</html>