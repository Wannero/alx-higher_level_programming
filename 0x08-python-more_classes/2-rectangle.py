{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x08-python-more_classes":{"items":[{"name":"0-rectangle.py","path":"0x08-python-more_classes/0-rectangle.py","contentType":"file"},{"name":"1-rectangle.py","path":"0x08-python-more_classes/1-rectangle.py","contentType":"file"},{"name":"101-nqueens.py","path":"0x08-python-more_classes/101-nqueens.py","contentType":"file"},{"name":"2-rectangle.py","path":"0x08-python-more_classes/2-rectangle.py","contentType":"file"},{"name":"3-rectangle.py","path":"0x08-python-more_classes/3-rectangle.py","contentType":"file"},{"name":"4-rectangle.py","path":"0x08-python-more_classes/4-rectangle.py","contentType":"file"},{"name":"5-rectangle.py","path":"0x08-python-more_classes/5-rectangle.py","contentType":"file"},{"name":"6-rectangle.py","path":"0x08-python-more_classes/6-rectangle.py","contentType":"file"},{"name":"7-rectangle.py","path":"0x08-python-more_classes/7-rectangle.py","contentType":"file"},{"name":"8-rectangle.py","path":"0x08-python-more_classes/8-rectangle.py","contentType":"file"},{"name":"9-rectangle.py","path":"0x08-python-more_classes/9-rectangle.py","contentType":"file"},{"name":"README.md","path":"0x08-python-more_classes/README.md","contentType":"file"}],"totalCount":12},"":{"items":[{"name":"0x00-python-hello_world","path":"0x00-python-hello_world","contentType":"directory"},{"name":"0x01-python-if_else_loops_functions","path":"0x01-python-if_else_loops_functions","contentType":"directory"},{"name":"0x02-python-import_modules","path":"0x02-python-import_modules","contentType":"directory"},{"name":"0x03-python-data_structures","path":"0x03-python-data_structures","contentType":"directory"},{"name":"0x04-python-more_data_structures","path":"0x04-python-more_data_structures","contentType":"directory"},{"name":"0x05-python-exceptions","path":"0x05-python-exceptions","contentType":"directory"},{"name":"0x06-python-classes","path":"0x06-python-classes","contentType":"directory"},{"name":"0x08-python-more_classes","path":"0x08-python-more_classes","contentType":"directory"},{"name":"0x09-python-everything_is_object","path":"0x09-python-everything_is_object","contentType":"directory"},{"name":"0x0A-python-inheritance","path":"0x0A-python-inheritance","contentType":"directory"},{"name":"0x0B-python-input_output","path":"0x0B-python-input_output","contentType":"directory"},{"name":"0x0C-python-almost_a_circle","path":"0x0C-python-almost_a_circle","contentType":"directory"},{"name":"0x0D-SQL_introduction","path":"0x0D-SQL_introduction","contentType":"directory"},{"name":"0x0E-SQL_more_queries","path":"0x0E-SQL_more_queries","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":15}},"fileTreeProcessingTime":4.869682999999999,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":649935575,"defaultBranch":"master","name":"alx-higher_level_programming","ownerLogin":"meriamemelkaoui","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-06-06T01:07:31.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/116093533?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1686015309.89986","canEdit":false,"refType":"branch","currentOid":"8e2dae017e721bcdbab9031528531dd330179e1c"},"path":"0x08-python-more_classes/2-rectangle.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","\"\"\"","New class Rectangle","\"\"\"","","","class Rectangle:","    \"\"\" Defines a rectangle \"\"\"","","    def __init__(self, width=0, height=0):","        self.width = width","        self.height = height","","    \"\"\" WIDTH \"\"\"","    @property","    def width(self):","        return (self.__width)","","    @width.setter","    def width(self, value):","        if type(value) != int:","            raise TypeError(\"width must be an integer\")","        if value < 0:","            raise ValueError(\"width must be >= 0\")","        self.__width = value","","    \"\"\" HEIGHT \"\"\"","    @property","    def height(self):","        return (self.__height)","","    @height.setter","    def height(self, value):","        if type(value) != int:","            raise TypeError(\"height must be an integer\")","        if value < 0:","            raise ValueError(\"height must be >= 0\")","        self.__height = value","","    \"\"\" Rectangle area \"\"\"","    def area(self):","        return (self.__height * self.__width)","","    \"\"\" Rectangle perimeter \"\"\"","    def perimeter(self):","        if self.width == 0:","            return (0)","        if self.height == 0:","            return (0)","        return (2 * (self.__height + self.__width))"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[{"start":0,"end":19,"cssClass":"pl-s"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":15,"cssClass":"pl-v"}],[{"start":4,"end":31,"cssClass":"pl-s"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":23,"end":28,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":29,"end":30,"cssClass":"pl-c1"},{"start":32,"end":38,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":28,"cssClass":"pl-s1"}],[],[{"start":4,"end":17,"cssClass":"pl-s"}],[{"start":4,"end":13,"cssClass":"pl-en"},{"start":5,"end":13,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":18,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":28,"cssClass":"pl-s1"}],[],[{"start":4,"end":17,"cssClass":"pl-en"},{"start":5,"end":10,"cssClass":"pl-s1"},{"start":11,"end":17,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":18,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-en"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":29,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":27,"cssClass":"pl-v"},{"start":28,"end":54,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":28,"cssClass":"pl-v"},{"start":29,"end":49,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":28,"cssClass":"pl-s1"}],[],[{"start":4,"end":18,"cssClass":"pl-s"}],[{"start":4,"end":13,"cssClass":"pl-en"},{"start":5,"end":13,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":19,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":29,"cssClass":"pl-s1"}],[],[{"start":4,"end":18,"cssClass":"pl-en"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":18,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":21,"end":26,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-en"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":29,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":27,"cssClass":"pl-v"},{"start":28,"end":55,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":28,"cssClass":"pl-v"},{"start":29,"end":50,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":29,"cssClass":"pl-s1"}],[],[{"start":4,"end":26,"cssClass":"pl-s"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-en"},{"start":13,"end":17,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":36,"cssClass":"pl-s1"},{"start":37,"end":44,"cssClass":"pl-s1"}],[],[{"start":4,"end":31,"cssClass":"pl-s"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":17,"cssClass":"pl-en"},{"start":18,"end":22,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":25,"end":26,"cssClass":"pl-c1"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":20,"end":21,"cssClass":"pl-c1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":20,"end":21,"cssClass":"pl-c1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":21,"end":25,"cssClass":"pl-s1"},{"start":26,"end":34,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-c1"},{"start":37,"end":41,"cssClass":"pl-s1"},{"start":42,"end":49,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/meriamemelkaoui/alx-higher_level_programming/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/meriamemelkaoui/alx-higher_level_programming/security/dependabot","repoSecurityAndAnalysisPath":"/meriamemelkaoui/alx-higher_level_programming/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"2-rectangle.py","displayUrl":"https://github.com/meriamemelkaoui/alx-higher_level_programming/blob/master/0x08-python-more_classes/2-rectangle.py?raw=true","headerInfo":{"blobSize":"1.13 KB","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"b8a3dd0","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fmeriamemelkaoui%2Falx-higher_level_programming%2Fblob%2Fmaster%2F0x08-python-more_classes%2F2-rectangle.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"50","truncatedSloc":"41"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/meriamemelkaoui/alx-higher_level_programming/discussions/new","newIssuePath":"/meriamemelkaoui/alx-higher_level_programming/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/meriamemelkaoui/alx-higher_level_programming/blob/master/0x08-python-more_classes/2-rectangle.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/meriamemelkaoui/alx-higher_level_programming/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/meriamemelkaoui/alx-higher_level_programming/raw/master/0x08-python-more_classes/2-rectangle.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"meriamemelkaoui","repoName":"alx-higher_level_programming","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"Rectangle","kind":"class","identStart":55,"identEnd":64,"extentStart":49,"extentEnd":1152,"fullyQualifiedName":"Rectangle","identUtf16":{"start":{"lineNumber":6,"utf16Col":6},"end":{"lineNumber":6,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":6,"utf16Col":0},"end":{"lineNumber":49,"utf16Col":51}}},{"name":"__init__","kind":"function","identStart":107,"identEnd":115,"extentStart":103,"extentEnd":197,"fullyQualifiedName":"Rectangle.__init__","identUtf16":{"start":{"lineNumber":9,"utf16Col":8},"end":{"lineNumber":9,"utf16Col":16}},"extentUtf16":{"start":{"lineNumber":9,"utf16Col":4},"end":{"lineNumber":11,"utf16Col":28}}},{"name":"width","kind":"function","identStart":239,"identEnd":244,"extentStart":235,"extentEnd":281,"fullyQualifiedName":"Rectangle.width","identUtf16":{"start":{"lineNumber":15,"utf16Col":8},"end":{"lineNumber":15,"utf16Col":13}},"extentUtf16":{"start":{"lineNumber":15,"utf16Col":4},"end":{"lineNumber":16,"utf16Col":29}}},{"name":"width","kind":"function","identStart":309,"identEnd":314,"extentStart":305,"extentEnd":517,"fullyQualifiedName":"Rectangle.width","identUtf16":{"start":{"lineNumber":19,"utf16Col":8},"end":{"lineNumber":19,"utf16Col":13}},"extentUtf16":{"start":{"lineNumber":19,"utf16Col":4},"end":{"lineNumber":24,"utf16Col":28}}},{"name":"height","kind":"function","identStart":560,"identEnd":566,"extentStart":556,"extentEnd":604,"fullyQualifiedName":"Rectangle.height","identUtf16":{"start":{"lineNumber":28,"utf16Col":8},"end":{"lineNumber":28,"utf16Col":14}},"extentUtf16":{"start":{"lineNumber":28,"utf16Col":4},"end":{"lineNumber":29,"utf16Col":30}}},{"name":"height","kind":"function","identStart":633,"identEnd":639,"extentStart":629,"extentEnd":845,"fullyQualifiedName":"Rectangle.height","identUtf16":{"start":{"lineNumber":32,"utf16Col":8},"end":{"lineNumber":32,"utf16Col":14}},"extentUtf16":{"start":{"lineNumber":32,"utf16Col":4},"end":{"lineNumber":37,"utf16Col":29}}},{"name":"area","kind":"function","identStart":882,"identEnd":886,"extentStart":878,"extentEnd":939,"fullyQualifiedName":"Rectangle.area","identUtf16":{"start":{"lineNumber":40,"utf16Col":8},"end":{"lineNumber":40,"utf16Col":12}},"extentUtf16":{"start":{"lineNumber":40,"utf16Col":4},"end":{"lineNumber":41,"utf16Col":45}}},{"name":"perimeter","kind":"function","identStart":981,"identEnd":990,"extentStart":977,"extentEnd":1152,"fullyQualifiedName":"Rectangle.perimeter","identUtf16":{"start":{"lineNumber":44,"utf16Col":8},"end":{"lineNumber":44,"utf16Col":17}},"extentUtf16":{"start":{"lineNumber":44,"utf16Col":4},"end":{"lineNumber":49,"utf16Col":51}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/meriamemelkaoui/alx-higher_level_programming/branches":{"post":"dNPBjSLQ8jifKCJV3AU8JzZVCP2Jt6RYzNVOoDlszQSZEtz9aJXfVupdKPoMyNXT4VH_ntYomC1LKqXJCvmmPw"},"/repos/preferences":{"post":"4KXpPA0IPGPtqUGTJwJPqnCespJDG_6nn7803ASCvhVme3hEngdNob6J0Ndz5aSDcwaWbud8KbbzXMZcCKABAQ"}}},"title":"alx-higher_level_programming/0x08-python-more_classes/2-rectangle.py at master · meriamemelkaoui/alx-higher_level_programming"}