CKEDITOR.plugins.add( 'filerimage', {
	lang: 'en,it',
	icons: 'filerimage',
	init: function( editor ) {
		lang = editor.lang.filerimage,
		editor.addCommand( 'filerImageDialog', new CKEDITOR.dialogCommand( 'filerImageDialog' ) );

		editor.ui.addButton( 'Filer Image', {
			label: lang.name,
			command: 'filerImageDialog',
			toolbar: 'insert',
			icon: 'filerimage'
		});

		if ( editor.contextMenu ) {
			editor.addMenuGroup( 'Filer' );
			editor.addMenuItem( 'imageItem', {
				label: lang.edit,
				icon: this.path + 'icons/filerimage.png',
				command: 'filerImageDialog',
				group: 'Filer'
			});

			editor.contextMenu.addListener( function( element ) {
				if ( element.getAscendant( 'img', true ) ) {
					return { imageItem: CKEDITOR.TRISTATE_OFF };
				}
			});
		}
		CKEDITOR.scriptLoader.load( this.path + '../../../../filer/js/popup_handling.js' );
		CKEDITOR.dialog.add( 'filerImageDialog', this.path + 'dialogs/filerImageDialog.js' );

		var dialog = CKEDITOR.dialog.getCurrent();
	}
});
