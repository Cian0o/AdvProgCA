var menu0 = [
 { 'Edit document': function(menuItem, menu) { editDocument(this.id) } },
 { 'Edit location': function(menuItem, menu) { editLocation(this.id) } }
];
 $(function() {
     $('.documentComposite_edit_icon').contextMenu(menu0, { theme: 'vista'
     });
 });

 var menu0a = [
 { 'Edit location': function(menuItem, menu) { editLocation(this.id) } }
];
 $(function() {
     $('.location_edit_icon').contextMenu(menu0a, { theme: 'vista'
     });
 });

var menu1 = [
 { 'Edit banner': function(menuItem, menu) { editBanner(this.id) } }
];
 $(function() {
 $('.banner_edit_icon').contextMenu(menu1, { theme: 'vista' });
 });


 var menu2 = [
 { 'Edit context group': function(menuItem, menu) { editContextGroup(this.id) } }
];
 $(function() {
     $('.contextGroup_edit_icon').contextMenu(menu2, { theme: 'vista' });
 });

 function editDocument(id) {
     for (var i = 0; i < editItems.length; i++) {
         if ((editItems[i].typeOfObject == 'documentComposite')
        && (editItems[i].id == id)
        ) {
             var url = editItems[i].editUrl + "DocumentsNew.aspx?fullPath=" + editItems[i].param2;
             editInAdmin(url)
         }
     }
 }

 function editLocation(id) {
     for (var i = 0; i < editItems.length; i++) {
         if ((editItems[i].typeOfObject == 'documentComposite')
        && (editItems[i].id == id)
        ) {
             var url = editItems[i].editUrl + "Locations.aspx?fullPath=" + editItems[i].param1;
             editInAdmin(url)
         }
     }
 }

 function editBanner(id) {
     for (var i = 0; i < editItems.length; i++) {
         if ((editItems[i].typeOfObject == 'banner')
        && (editItems[i].id == id)
        ) {
             var url = editItems[i].editUrl ;
             editInAdmin(url)
         }
     }
 }

 function editContextGroup(id) {
     for (var i = 0; i < editItems.length; i++) {
         if ((editItems[i].typeOfObject == 'contextGroup')
        && (editItems[i].id == id)
        ) {
             var url = editItems[i].editUrl;
             editInAdmin(url)
         }
     }
 }

 var editItems = new Array();
 function EditItem(typeOfObject, id, editUrl, param1, param2) {
     this.typeOfObject;
     this.id;
     this.editUrl;
     this.param1;
     this.param2;

     this.typeOfObject = typeOfObject;
     this.id = id;
     this.editUrl = editUrl;
     this.param1 = param1;
     this.param2 = param2;

 }
 var editModeWin;
 function editInAdmin(url) {
     var WinSettings = "center:yes;resizable:no;dialogHeight:700px"
     editModeWin = window.open(url, "ECM"); //WinSettings
     editModeWin.focus();
     setTimeout('editModeWin.focus()', 1000);
 }    
