<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;

class CreateSubscriptionItemsTable extends Migration {

	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up()
	{
		Schema::create('subscription_items', function(Blueprint $table)
		{
			$table->integer('id', true);
			$table->integer('subscription_id')->index('fk_subscription_items_1_idx');
			$table->string('product_serial_number', 45);
			$table->string('product_description', 45);
			$table->float('product_price', 10, 0);
			$table->timestamps();
			$table->softDeletes();
		});
	}


	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down()
	{
		Schema::drop('subscription_items');
	}

}
